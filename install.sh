#!/bin/bash
yum install python3 wget -y
wget -P /tmp/ https://mirror.fastspeedgo.xyz/V2rayWithWebControl/setup.py
pip3 install flask pymysql requests
/usr/bin/python3 /tmp/setup.py
