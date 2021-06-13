#!/bin/bash
#@Author prince kumar
#Date 25 may 2021
apt update && apt upgrade
pkg install python
pkg install python2
pkg install python3
pip3 install pytube
cat you_d.py >> You_d 
chmod +x You_d 
mv You_d ~
cd 
mv You_d ..
cd ..
mv You_d usr/bin
echo -e "\e[32;1m Now type You_d -h for uses "

