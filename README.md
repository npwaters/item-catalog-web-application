# Project 4 - Item Catalog - Web Application
The Item Catalog Web Application provides a list of items within a variety of categories as well as provide
 a user registration and authentication system. Registered users will have the ability to post,
  edit and delete their own items.


### Installation
Fork the 'item-catalog-web-application' GitHub repository

Clone the forked repository to your Linux machine

    (venv) vagrant@vagrant:~/apps$ git clone https://github.com/npwaters/item-catalog-web-application.git catalog

Create a new virtual environment

    vagrant@vagrant:~/apps/catalog$ python3 -V
    Python 3.5.2
    vagrant@vagrant:~/apps/catalog$ python3 -m venv venv

Install the project package requirements

    vagrant@vagrant:~/apps/catalog$ source venv/bin/activate
    (venv) vagrant@vagrant:~/apps/catalog$ pip install -r requirements.txt

Configure a secret key

    (venv) vagrant@vagrant:~/apps/catalog$ echo -e "SECRET_KEY = '[your secret key]'\nGOOGLE_OAUTH_API_CLIENT_ID = '[your Google OAuth API client ID]'"  > settings.py

Set environment variables

    VAGRANT_PASSWORD=[your database user password]
    DB_IP=[your database server IP address/hostname]

Create the database

    vagrant@vagrant:~/apps/catalog$ createdb catalog 

Configure Google OAuth API application in the Google Developer Console

https://developers.google.com/identity/protocols/OAuth2WebServer#prerequisites 

Save 'client_secret.json' to '\[project root\]/authentication' 



 
### Environment
Python 3.5.2 on Linux

### Usage

#### Seeding the database 
The database can be seeded using 'create_catalog_items.py'. The source file is <br>
'catalog_data.txt'.<br>
Catalog item attributes are delimited by a pipe "|" character.<br> 
Category names are on lines with no delimiter.<br>
All catalog item lines following a category line will be associated with the category.<br>
User 1 will be associated with category and related items when the number of categories is an odd number, <br>
User 2 when an even number.


#### Starting the Item Catalog

The command below starts the web application such that it can be accessed remotely port 5004

    vagrant@vagrant:~/apps/catalog$ flask run --host=0.0.0.0 --port=5004


#### Accessing the Item Catalog

Assuming Flask has been started as above:<br>

Item catalog home page - 'http://[your web server hostname/IP]:5004'<br>
JSON API endpoint - 'http://[your web server hostname/IP]:5004/catalog/items'

The JSON API endpoint returns all catalog items grouped by category, including category details.

