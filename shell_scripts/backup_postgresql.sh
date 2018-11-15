#/bin/bash
# auto backup postgresql
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin;
export PATH

function backup(){
  if [ -e "/home/ubuntu/postgresql_backup.sql" ]; then
	mv /home/ubuntu/postgresql_backup.sql /home/ubuntu/old_backup/postgresql_backup.sql
  fi
  if ! [ -e "/home/ubuntu/postgresql_backup.sql" ]; then
	echo $(date) >> /home/ubuntu/post_log
	echo "backup begin" >> /home/ubuntu/post_log
    
    export PGPASSWORD=PASSWORD																
    pg_dump -U pgadmin -h ProductionHost -p 5432 ProductionDB -c -f /home/ubuntu/postgresql_backup.sql
    
	echo $(date) >> /home/ubuntu/post_log
	echo "backup end" >> /home/ubuntu/post_log
	echo >> /home/ubuntu/post_log
  fi
}

function restore(){
  if [ -e "/home/ubuntu/postgresql_backup.sql" ]; then
	echo $(date) >> /home/ubuntu/post_log
	echo "restore begin" >> /home/ubuntu/post_log
    
    export PGPASSWORD=PASSWORD																
   	psql -U pgadmin -h TestHost -d TestDB -p 5432 -f /home/ubuntu/postgresql_backup.sql
    
	echo $(date) >> /home/ubuntu/post_log
	echo "restore end" >> /home/ubuntu/post_log
	echo >> /home/ubuntu/post_log
  fi
}

backup && restore && echo "backup & restore end normally." >> /home/ubuntu/post_log
echo $(date) >> /home/ubuntu/post_log
echo >> /home/ubuntu/post_log 