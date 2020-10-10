# drcom_guet
drcom python auto login script for guet
# GayUET哆点自动登录
### guet使用哆点d版但是drcom无法发挥作用，于是对drcom作简单适配
# python版（适用于电脑）
### windows和linux都可正常使用（目前在Windows上测试正常）
## 如何使用
#### 编辑以下代码，将学号和密码和登录类型替换为自己的即可
```
user = "19003xxxxx"
#学号
pwd = "xxxxxx"
#密码
type = 3
# 0,1,2,3分别对应校园网、移动、联通与电信。
```
# bash版（可放在路由器上）
#### 编辑以下代码，然后上传到路由器/usr/bin（openwrt）目录下
```
number=19003xxxxx
pwd=123456
```

#### 然后给权限，将drcom_guet.sh添加到/etc/rc.local的exit前
`chmod /usr/bin/drcom_guet.sh`
