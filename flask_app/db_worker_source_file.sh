#Run this file on workers that will connect to MariaDB backend
#Information regarding host, database, user, and path to files
export DB_HOST_ADDRESS=192.168.1.63
export DB_DATABASE_NAME=test_insert
export DB_USER_WORKER=felix_external
export PATH_TO_WORKER_RESULTS=/home/ubuntu/test_results/
#Password for 'DB_USER'
echo "Please enter Password for DB_USER: $DB_USER "
read -sr DB_USER_PASSWORD_INPUT
export DB_PASSWORD_WORKER=$DB_USER_PASSWORD_INPUT
