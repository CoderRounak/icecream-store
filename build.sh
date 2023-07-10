#!/bin/bash
# install dependency
pip install -r build.sh

# migration
py manage.py migrate

