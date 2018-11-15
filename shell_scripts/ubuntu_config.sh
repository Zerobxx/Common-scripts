#!/bin/bash
#

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin;
export PATH

# enable ipv4 precedence
if ! grep '^precedence ::ffff:0:0/96  100' /etc/gai.conf; then
    echo 'precedence ::ffff:0:0/96  100' >> /etc/gai.conf
fi

# increase the num of file descriptor
if ! grep '^ulimit -n 65535' ~/.profile; then
    echo 'ulimit -n 65535' >> ~/.profile
    source ~/.profile
fi


# config ssh can only use public key to log in
config_ssh() {
    
    # disable passowrd
    if grep '^PasswordAuthentication' /etc/ssh/sshd_config; then
        sed -re 's/^(PasswordAuthentication)([[:space:]]+)yes/\1\2no/' -i.`date -I` /etc/ssh/sshd_config
    else
        echo PasswordAuthentication no >> /etc/ssh/sshd_config
    fi
    
    # input the public keys
    if [ ! -d "~/.ssh" ]; then
        mkdir ~/.ssh
        cd ~/.ssh
        echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDbuBUBN+ruO4bSNMby4F3l8kT33rCr2KnjOT7k+UhjPBJqNSLIJL5EGNEWBeFAnVOZZ3ED0T/SeCerqdUr+CdM8GKQ3o+v6rC7ZS3KiSZSeGy2s8W04xiny/jnYoolzRo5uXQmj3gWOPPcoOVDhKR3ypOsFTVdTs9/EW0dw01Z2lHvf2XkFq7oa9Q4Ss5a5CoT9Qwtgh/CT3HoziFVrZ6ZBhDsTdnEQl3o8Yg2AO/LzPfNBRG603lqHN6MnARaYJIPLogknUDWvUId/A/dB/kWdgHNxHrkf77XgbLxg/J1QFgS5lHqZotGYhATV4fyX22lVEaYteO0qnONTsDTsuMb zerobxx@163.com >> authorized_keys
        chmod 600 authorized_keys
        service sshd restart
    fi
}

config_ssh