#!/bin/bash
# rotate the logs 

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin;
export PATH

# the logs path can be input by command line or pipe(by xargs)
log_path=/data/logs/out.log


log_rotate() {
    
    # create a backup daily
    # the shell script will be excuted at 1.am everyday
    cp ${logs_path} ${logs_path}.$(date -d "yesterday" +"%Y%m%d")
    
    # override the original log file by using > to create a new empty log file
    > ${logs_path}
    
    # delete the old log files which existed more than 3 days
    rm -f ${logs_path}.$(date -d "3 days ago" +"%Y%m%d")
}  

log_rotate