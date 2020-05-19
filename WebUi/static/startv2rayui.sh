#!/bin/bash
nohup /usr/bin/python3 /V2rayWithWebControl/main.py > /V2rayWithWebControl/main.log 2>&1 & echo $! > /V2rayWithWebControl/process.pid &
