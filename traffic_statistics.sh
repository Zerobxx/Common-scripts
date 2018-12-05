#!/bin/bash
# calculate by /proc/net/dev

ethn=eth0

RX=$(cat /proc/net/dev | grep $ethn | sed 's/:/ /g' | awk '{print $2}')
TX=$(cat /proc/net/dev | grep $ethn | sed 's/:/ /g' | awk '{print $10}')

TOTAL=$((${RX}+${TX}))

MIN=`TZ=UTC-8 date +"%Y%m%d%H%M"`
Last_MIN=`TZ=UTC-8 date +"%Y%m%d%H%M" -d "1 minutes ago"`
TODAY=`TZ=UTC-8 date +"%Y%m%d"`

redis-cli SET total.${MIN} $TOTAL EX 172800
# redis-cli expire total.${MIN} 172800

Last_TOTAL=`redis-cli GET total.${Last_MIN}`

if [[ $Last_TOTAL ]]; then

    Current_min_traffic=$((${TOTAL}-${Last_TOTAL}))
    redis-cli SET ${Last_MIN} $Current_min_traffic EX 172800
    # redis-cli expire ${Last_MIN} 172800
    
    Today_Current=`redis-cli GET ${TODAY}`
    Today_TOTAL=$((${Today_Current}+${Current_min_traffic}))
    redis-cli SET ${TODAY} $Today_TOTAL
    
fi