#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# @Author  : chainsx,libfrozen
# @FileName: drcom_guet.py

import json
import requests
import math
import random
from time import sleep
from subprocess import run, PIPE

#学号
user = "2000******"
#密码
pwd = "NikaidouShinkuDaisuki"
# 0,1,2,3分别对应校园网、移动、联通与电信。
type = 3

login_type=['', '@cmcc', '@unicom', '@telecom']

def login(user, pwd, type):
    url = "http://10.0.1.5/drcom/login"
    data = {
        'callback': 'dr1003',
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
        'jsVersion': '4.2',
        'v': math.floor(random.random()*10000+500),
        'lang': "zh"
        }
    res = requests.get(url, params=data).text
    res = res.split('(')[1].split(')')[0]
    res = json.loads(res)

    if res['result'] == 1:
        print(res['uid'] + " 登录成功")
        print("系统分配的IP地址是" + res['v46ip'])

cnt = 1
while True:
    r = run('ping 223.5.5.5',
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            shell=True)
    if r.returncode:
        print('登录尝试第{}次'.format(cnt))
        login(user, pwd, type)
        cnt += 1
    else:
        print('正常联网')
    sleep(60*30)
