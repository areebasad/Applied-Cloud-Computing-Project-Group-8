export DB_WORKER_HOST=localhost
export DB_DATABASE_NAME=test_insert
export DB_USER=felix_root

echo "Please enter Password for DB_USER: $DB_USER "
read -sr DB_USER_PASSWORD_INPUT
export DB_USER_PASSWORD=$DB_USER_PASSWORD_INPUT

export PATH_TO_WORKER_RESULTS=/home/ubuntu/test_results/
