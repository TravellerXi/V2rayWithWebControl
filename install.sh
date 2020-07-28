#!/bin/bash
yum install python3 wget -y
wget -P /tmp/ https://mirror.fastspeedgo.xyz/V2rayWithWebControl/setup.py
/usr/bin/python3 /tmp/setup.py
