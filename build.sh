#!/bin/bash
# install dependency
pip install -r requirements.txt

# migration
python manage.py migrate

