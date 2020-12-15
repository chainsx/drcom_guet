#!/bin/ash
time=$(date +%s%3N)
number=19003xxxxx
pwd=xxxxxx
HOST=10.70.121.254
#touch /tmp/networkstatus.log
ping -c 4 "$HOST" > /dev/null
if [ $? -eq 0 ];then
        echo "check final" >> /tmp/networkstatus.log
else
        curl "http://10.32.254.11/drcom/login?callback=dr$time&DDDDD=$number&upass=$pwd&0MKKey=123456&R1=0&R3=1&R6=0&para=00&v6ip=&_=$time"
        #touch /tmp/networkstatus.log
        echo "final" >> /tmp/networkstatus.log
fi
