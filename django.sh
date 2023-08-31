#!/bin/bash

echo "Creating Migrations..."
python backend/manage.py makemigrations 
echo ====================================

echo "Starting Migrations..."
python backend/manage.py migrate
echo ====================================

echo "Starting Server..."
python backend/manage.py runserver 0.0.0.0:8000
