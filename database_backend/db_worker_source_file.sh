#Run this file on workers that will connect to MariaDB backend
#Information regarding host, database, user, and path to files
export DB_WORKER_HOST=localhost
export DB_DATABASE_NAME=test_insert
export DB_USER=felix_root
export PATH_TO_WORKER_RESULTS=/home/ubuntu/test_results/
#Password for 'DB_USER'
echo "Please enter Password for DB_USER: $DB_USER "
read -sr DB_USER_PASSWORD_INPUT
export DB_USER_PASSWORD=$DB_USER_PASSWORD_INPUT
