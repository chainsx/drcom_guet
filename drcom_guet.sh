#!/bin/bash
uid=2000********
carrier=3
pwd=NikaidouShinkuDaisuki
HOST=223.5.5.5
#touch /tmp/networkstatus.log
for((i=0;i<${#pwd};i++))
do
    case ${pwd:$i:1} in
    \ )
        pwd2=${pwd2}"%20";;
    \")
        pwd2=${pwd2}"%22";;
    \#)
        pwd2=${pwd2}"%23";;
    \%)
        pwd2=${pwd2}"%25";;
    \&)
        pwd2=${pwd2}"%26";;
    \()
        pwd2=${pwd2}"%28";;
    \))
        pwd2=${pwd2}"%29";;
    \+)
        pwd2=${pwd2}"%2B";;
    \=)
        pwd2=${pwd2}"%3D";;
    \@)
        pwd2=${pwd2}"%40";;
    *)
        pwd2=${pwd2}${pwd:$i:1};;
    esac
done
case $carrier in
1)  uid=${uid}"%40cmcc";;
2)  uid=${uid}"%40unicom";;
3)  uid=${uid}"%40telecom";;
*)  uid=${uid};;
esac
ping -c 4 "$HOST" > /dev/null
if [ $? -eq 0 ];then
        echo "check final" >> /tmp/networkstatus.log
else
        result=`curl "http://10.0.1.5/drcom/login?callback=dr1003&DDDDD=$uid&upass=$pwd2&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.2&v=$RANDOM&lang=zh"`
        echo $result
        #touch /tmp/networkstatus.log
        echo "final" >> /tmp/networkstatus.log
fi

