# NO DOCKER

sudo apt install python3-pip python3-venv
python3 -m pip install --upgrade pip

python3 -m venv venv
. ./venv/bin/activate

pip install -r ./app/requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate --noinput
python3 manage.py runserver 0.0.0.0:8000
