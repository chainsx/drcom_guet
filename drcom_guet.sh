#!/bin/ash

time=$(date +%s%3N)
number=1900301019
pwd=123456
curl "http://10.32.254.11/drcom/login?callback=dr$time&DDDDD=$number&upass=$pwd&0MKKey=123456&R1=0&R3=1&R6=0&para=00&v6ip=&_=$time"
