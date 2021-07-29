#!/bin/sh
sudo apt install python3-pip python3-venv nginx
python3 -m pip install --upgrade pip

# Ajouter copie config NGINX
# Ajouter fichier Service Web

python3 -m venv ../venv
. ../venv/bin/activate

pip install -r ../app/requirements.txt

python3 ../app/manage.py makemigrations
python3 ../app/manage.py migrate --noinput
python3 ../app/manage.py runserver 0.0.0.0:8000
