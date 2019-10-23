#Configuring the RabbitMQ-broker
On the 'master' VM install RabbitMQ-server and other needed libraries for Python:
```
sudo apt-get install rabbitmq-server -y
sudo pip3 install celery
sudo pip3 install Flask
```
In order to get the workers to connect to the Broker you need to set up a rabbitMQ user and virtual host.
Do the following on the RabbitMQ-server:
*(it This will create a rabbitMQ user named <YOURUSER> RabbitUser with a vhost <YOURVHOST>)*
```
rabbitmqctl add_user <YOURUSER> <YOURPASSWORDHERE>
rabbitmqctl add_vhost <YOURVHOST>
rabbitmqctl set_user_tags <YOURUSER> administrator
rabbitmqctl set_permissions -p <YOURVHOST> <YOURUSER> ".*" ".*" ".*" 
rabbitmqctl delete_user guest #Not necessary
```
*(To set up the broker properly for the Celery worker add)*
In the code for Celery broker you should write:
```
'amqp://<user>:<password>@<ip>/<vhost>'
```



#Downloading and installing Docker:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt-get update
apt-cache policy docker-ce #not necessary
apt-get install -y docker-ce
systemctl status docker #Not necessar
```