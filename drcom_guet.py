#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# @Author  : chainsx
# @FileName: drcom_guet.py

import time
import json
import requests
from time import sleep
from subprocess import run, PIPE

user = "190030xxxx"
#学号
pwd = "xxxxxxxx"
#密码
type = 3
# 0,1,2,3分别对应校园网、移动、联通与电信。

login_type=['', '@cmcc', '@unicom', '@telecom']

def login(user, pwd, type):
    url = "http://10.0.1.5/drcom/login"
    data = {
        'callback': 'dr' + str(int(time.time() * 1000)),
        'DDDDD': user + login_type[type],
        'upass': pwd,
        '0MKKey': '123456',
        'R1': '0',
        'R2': None,
        'R3': '0',
        'R6': '0',
        'para': '00',
        'v6ip': None,
        'terminal_type': '1',
        'lang': 'zh-cn',
        'jsVersion': '4.1',
        'v': '6471',
        }
    res = requests.get(url, params=data).text
    res = res.split('(')[1].split(')')[0]
    res = json.loads(res)

    if res['result'] == 1:
        print(res['uid'] + " login success")
        print("your ip address is " + res['v46ip'])

cnt = 1
while True:
    r = run('ping www.guet.edu.cn',
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            shell=True)
    if r.returncode:
        print('relogin 第{}次'.format(cnt))
        login(user, pwd, type)
        cnt += 1
    else:
        print('正常联网')
    sleep(60*30)
