# logAnalysis Project 

## Description
  The Log analysis project by  Udacity

## Reproduce
```
requirements

Ubuntu/debian OS


ckage          Version 
---------------- --------
certifi          2019.3.9
chardet          3.0.4   
Click            7.0     
docopt           0.6.2   
Flask            1.0.2   
grip             4.5.2   
idna             2.8     
itsdangerous     1.1.0   
Jinja2           2.10.1  
Markdown         3.1     
MarkupSafe       1.1.1   
path-and-address 2.0.1   
pip              19.0.3  
psycopg2         2.7.7   
psycopg2-binary  2.8     
Pygments         2.3.1   
requests         2.21.0  
setuptools       40.8.0  
urllib3          1.24.1  
Werkzeug         0.15.2  
wheel            0.33.1  



Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> record = "This is a record"
>>> print(f"you are connected to - {record}")
you are connected to - This is a record



```

### Changes made 
+ I am running this project on a linux machine which has Postgres and python installed, I do not need to install VirtualBox or Vagrant for that matter, which makes it simpler 
+ I Change the newsdata.sql, All vagrant owners are changed to postgres, as my superUser is "postgres", very few changes made here, some 6-7 lines need to be changed inside newsdata.sql
+ I ceate the db "news" with postgres su
+ use postgres as your superuser to push the commands into news database as below, the changed newsdata.sql is present inside the folder newsdata
```
deploy@hopperTestRemote:~/logsAnalysis/newsdata$ sudo -u postgres psql -d news -f newsdata.sql 
```

#### If you see the error connecting to the news database through psycopg2, "password authentication failed for Postgres"

```
1. sudo -u postgres psql

If that fails with a database "postgres" does not exists error, then you are most likely not on a Ubuntu or Debian server :-) In this case simply add template1 to the command:

sudo -u postgres psql template1

If any of those commands fail with an error psql: FATAL:  password authentication failed for user "postgres" then check the file /etc/postgresql/8.4/main/pg_hba.conf: 
There must be a line like this as the first non-comment line:

local   all         postgres                          ident
For newer versions of PostgreSQL ident actually might be peer, if you need you can change this to trust. That's OK also.

Inside the psql shell you can give the DB user postgres a password:

2. ALTER USER postgres PASSWORD 'newPassword';
You can leave the psql shell by typing CtrlD or with the command \q.


3. sudo service postgresql restart

```


## Results

  + What are the most popular three articles of all time ?
  ```
  "candidate-is-jerk" -- 338647 views
  "bears-love-berries" -- 253801 views
  "bad-things-gone" -- 170098 views
  ```
  
  + Who are the most popular article authors of all time ?
  ```
  Rudolf von Treppenwitz -- 338647 views
  Ursula La Multa -- 253801 views
  Anonymous Contributor -- 170098 views
  ```
  
  + On which days did more than 1% of requests lead to errors ?
  ```
  Jul 17, 2016 --  2.3% errors
  ```


## Helpful Links
+ https://linuxize.com/post/how-to-install-postgresql-on-debian-9/
