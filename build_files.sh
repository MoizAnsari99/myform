python3 -m ensurepip --default-pip
python3 -m pip --version

python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
