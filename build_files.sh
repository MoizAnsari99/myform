#!/bin/bash

# Install dependencies using Python's module call
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Collect static files for Django
python3 manage.py collectstatic --noinput
