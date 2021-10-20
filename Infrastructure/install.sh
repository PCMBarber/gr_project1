#!/bin/bash
sudo apt-get update
sudo apt install -y python3 python3-pip gunicorn
git clone https://github.com/PCMBarber/gr_project1.git
cd ./gr_project1/flask_project
SECRET_KEY=gdsfejhkbljkhgsdrelhjkbdgsrew
export SECRET_KEY
pip3 install -r requirements.txt
python3 create.py
gunicorn -D --workers=4 --bind=0.0.0.0:5000 app:app