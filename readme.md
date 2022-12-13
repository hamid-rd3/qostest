#


## create and start a rabbitmqserver server
```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install erlang
sudo apt-get install rabbitmq-server
#default port is 5672
sudo service rabbitmq-server enable or sudo systemctl enable rabbitmq-server
sudo service  rabbitmq-server start or sudo systemctl start rabbitmq-server
##user is the username and password is the new password
sudo rabbitmqctl add_user user password
##giving that user adiministraitve rights
sudo rabbitmqctl set_user_tags user administrator
sudo rabbitmqctl set_permissions -p / user "." "." "."
```
## start a postgresql server
```bash
sudo su — postgres
psql
create user myprojectuser;create database myproject;alter role hero with password 'password';grant all privileges on database myproject to myprojectuser;alter database myproject owner to myprojectuser;
##connect to database default poer is 5432
psql -U myprojectuser -h 127.0.0.1 myproject
```

**On Linux or WSL**
```bash
pip install virtualenv
python3 -m venv .venv
source .venv/bin/activate 
#to ensure your environment activation you can check by :
which python
```
**Install the requirement packeges**
```bash
pip install -r requirements.txt
chmod +x install_required.sh
./install_required.sh
```
### Add an admin user


**Admin and create QoS objects**
```bash
cd backend 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
##Register with your desired username and password

```
**Start server**
```bash
#default port 8000 select another port if you want   
python manage.py runserver 8000
```

python manage.py dumpdata > whole.json
