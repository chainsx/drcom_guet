# G(ay)UET哆点校园网自动登录

#### 我对于桂电晚上不断网对于校园网流量不限制的做法十分满意并十分感谢！！！
## 关于
#### guet使用哆点d版但是drcom无法发挥作用，于是对drcom作简单适配
#### 通过抓包发现桂电的哆点登录方式奇特，可简化为后面的bash脚本

# 如何使用
#### 只需运行一次脚本登录即可
## python版（适用于电脑或路由器直连校园网的情况）
### windows和linux都可正常使用

#### 编辑以下代码，将学号和密码和登录类型替换为自己的即可
```
user = "19003xxxxx"
#学号
pwd = "xxxxxx"
#密码
type = 3
# 0,1,2,3分别对应校园网、移动、联通与电信。
```
## bash版（简化登录版，可放在路由器上）
#### 编辑以下代码，然后上传到路由器/usr/bin（openwrt）目录下
```
number=19003xxxxx
pwd=123456
```
#### 然后给权限，将drcom_guet.sh添加到/etc/rc.local的exit前
`chmod /usr/bin/drcom_guet.sh`

#### pdcn（老毛子）可以在自定义脚本里面讲bash文件内容复制到“在wan启动之后运行”的脚本里面以实现自动登录
#### openwrt可以使用`crontab -e` 添加 `* * * * * /usr/bin/login.sh` 每分钟检测一次

# 转载请注明
