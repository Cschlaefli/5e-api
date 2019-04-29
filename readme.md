This is a simple python eve project that provides an API for the 5th edition SRD for Dungeons and Dragons. It includes a modified verision of eve-docs to provide information on the API endpoints

It does not include the mongodb databases with the actual SRD information, I have collected them here https://github.com/Cschlaefli/5e-db


##Requirements

Mongodb
Virtualenv

##Installation

It relys on a mongodb instance running on the default port on the same machine, which you can change in the settings.py. If you want the database populated, make sure you have a mongodb instance running, then clone the 5e-db repository and run mongorestore.
```cd 5e-db
mongorestore -db 5e-dnd
```

it's easiest if you clone the repository into /var/www/, otherwise you will need to change the path in the wsgi.ini file and 5e-api script to point to the actual location. 
```cd /var/www/
sudo git clone https://github.com/Cschlaefli/5e-api
```

To actually run the api, you need to first install virtualenv

Create a virtualenv named env in the cloned repository, and install the requirements.txt to the env
(as root)
```cd 5e-api
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
pip3 install eve_docs/setup.py
```
The last line is to install my branch of eve_docs included in the repo


It also runs by default as www, so you'll need to create that system user and change the ownership of 5e-api for it to run, if you want to run it as a different user, just change the gid and uid in the wsgi.ini
```
sudo useradd -r www
chown -R www:www 5e-api
```

Then the 5e-api script will run the application on wsgi port :5000, which you can use nginx or apache to forward traffic to. If you want to expose the wsgi application directly, change the wsgi.ini line
`port = :5000`
to
`http-port = :PortNumber`

The docs are exposed by default at /docs, if you want to allow more CRUD functionality, change it in the api_5e settings.py following the [python eve docs](https://docs.python-eve.org/en/stable/config.html)

