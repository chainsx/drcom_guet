#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# @Author  : chainsx
# @FileName: drcom_guet.py

import time
import socket
import json
import requests

login_type=['', '@cmcc', '@unicom', '@telecom']

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('guet.edu.cn', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
myaddr = get_host_ip()

def login(user, pwd, type):
	url = "http://10.32.254.11:801/eportal/"
	data = {
		'c': 'Portal',
		'a': 'login',
		'callback': 'dr' + str(int(time.time() * 1000)),
		'login_method': '1',
		'user_account': user + login_type[type],
		'user_password': pwd,
		'wlan_user_ip': myaddr,
		'wlan_user_ipv6': '',
		'wlan_user_mac': '000000000000',
		'wlan_ac_ip': '',
		'wlan_ac_name': '',
		'jsVersion': '3.3',
		'_': str(int(time.time() * 1000)),
		}
	res = requests.get(url, params=data).text
	res = res.split('(')[1].split(')')[0]
	res = json.loads(res)
	if res['msg'] == '':
		print('UNKNOWN ERROR')
	print(res)


user = "19003xxxxx"
#学号
pwd = "xxxxxxx"
#密码
type = 3
# 0,1,2,3分别对应校园网、移动、联通与电信。

login(user, pwd, type)
