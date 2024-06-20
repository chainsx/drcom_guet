# 桂林（电）子（科技）大学校园网自动登录
#### 基于 chainsx 的 drcom_guet 项目修改而来，针对新的参数以及一些特殊字符做了适配
#### 晚上推真红老婆再也不怕突然断网了！（

# 如何使用
#### 只需运行一次脚本登录即可
## python版（适用于电脑或路由器直连校园网的情况）
### windows和linux都可正常使用

#### 编辑以下代码，将学号和密码和登录类型替换为自己的即可
```
#学号
user = "2000xxxxxx"
#密码
pwd = "NikaidouShinkuDaisuki"
# 此处type的值设为0,1,2,3分别对应以校园网、移动、联通或电信用户登录。
type = 3

```
## bash版（简化登录版，可放在路由器上）
#### 编辑以下代码，然后上传到路由器/usr/bin（openwrt）目录下，uid为学号，pwd为上网登录密码（目前跟统一认证系统密码一致）
```
uid=2000xxxxxx
pwd=NikaidouShinkuDaisuki
```
#### 然后给权限，将drcom_guet.sh添加到/etc/rc.local的exit前
`chmod /usr/bin/drcom_guet.sh`

#### pdcn（老毛子）可以在自定义脚本里面讲bash文件内容复制到“在wan启动之后运行”的脚本里面以实现自动登录
#### openwrt可以使用`crontab -e` 添加 `* * * * * /usr/bin/login.sh` 每分钟检测一次

# 转载请注明所有作者
