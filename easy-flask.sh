#!/bin/bash
echo -e "\033[33m ---------- 1/3 Install ---------- \033[0m"
echo
sudo apt install python-pip 
sudo pip install flask

echo -e "\033[33m ---------- 2/3 Download ---------- \033[0m"
echo
mkdir -p ~/easy-flask
wget -P ~/easy-flask https://raw.githubusercontent.com/PengJenas/easy-flask/master/index.html --no-check-certificate
wget -P ~/easy-flask https://raw.githubusercontent.com/PengJenas/easy-flask/master/easy-flask.py --no-check-certificate

echo -e "\033[33m ---------- 3/3 Run ---------- \033[0m"
echo
nohup python -u ~/easy-flask/easy-flask.py --port=80 >~/easy-flask/log 2>&1 &

ip=$(curl -4 ip.sb)
echo -e "\033[33m Now visit: \033[0m\033[4;31mhttp://${ip}:80/\033[0m"
echo
