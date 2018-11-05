#!/bin/bash
#

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin;
export PATH

read -p "File name:" fileName

if [ ! -f "./$fileName" ]; then
    touch ${fileName}.txt
    echo "File head " >>${fileName}.txt
    read -p "Variable:" variableName
    echo "variable=$variableName" >>${fileName}.txt
    echo "File tail" >>${fileName}.txt
fi