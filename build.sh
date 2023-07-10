#!/bin/bash
# install dependency
pip install -r requirements.txt

# migration
py manage.py migrate

