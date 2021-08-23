#Book_repository

flask application where user can find information about books by searching book isbn.
user needs to login to make searches.
new users can register if they don't have longin credentials.

setup
1. run $pip3 install -r requirement.txt
2. run $sudo apt-get install python3-psycopg2
3. $export FLASK_APP=application
4. $export DATABASE_URL={database connecting string}      eg. postgresql:username:password@localhost:5432/databasename
5. run $python3 import.py
6. $flask run

#technologies used
    flask framework for server;
    postgresql as database;
    sqlalchemy as orm;
    jinja2;
    html;
    bootstrap;
