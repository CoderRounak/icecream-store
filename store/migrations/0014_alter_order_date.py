# Generated by Django 4.0.4 on 2023-07-10 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 10, 19, 26, 24, 491512)),
        ),
    ]
