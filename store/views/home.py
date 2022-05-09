from django.shortcuts import render, redirect
from store.models.category import Category
from store.models.product import Product
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = None
        categories = Category.get_all_categories()
        category_ID = request.GET.get('category')
        if category_ID:
            products = Product.get_all_products_id(category_ID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories

        return render(request, 'index.html', data)

    def post(self, request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1

                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1

        request.session['cart']=cart

        return redirect('homepage')
