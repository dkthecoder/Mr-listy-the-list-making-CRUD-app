#/bin/bash

sudo apt install python3 python3-pip git -y

sudo pip3 install -r requirements.txt

export DB_HOST = 35.230.155.133
export USER = root
export PASSWORD = root
export DATABASE = mrlistyflaskdb

export SECRET_KEY = 44ea3dab727dfa24322ca91c30854073

./python3 run.py

#python3 -m pytest --cov=application
#echo 'TESTNG:'
#python3 -m pytest --cov=application --cov-report=term-missing html
