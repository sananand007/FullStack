# logAnalysis Project 

## Description
  The LogAnalysis project queries a mock database called "news" using Postgres and psycopg2 to get sensible metrics for a news website.
  After querying it provides the data as a cosolidated output

## Reproduce
```
requirements

Ubuntu/debian OS

Python version - 3.6

ckage          Version 
---------------- --------
certifi          2019.3.9
pip              19.0.3  
psycopg2         2.7.7   
psycopg2-binary  2.8     
setuptools       40.8.0    



Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> record = "This is a record"
>>> print(f"you are connected to - {record}")
you are connected to - This is a record
```

### Changes made to run the project
+ Run this project on a linux machine which has Postgres and python installed, we do not need to install VirtualBox or Vagrant for that matter, which makes it simpler 
+ Change the newsdata.sql, All vagrant owners are changed to postgres, as my superUser is "postgres"
+ Ceate the db "news" with postgres su
+ Use postgres as your superuser to push the commands into news database as below, the changed newsdata.sql is present inside the folder newsdata
+ Copy the newsdata.zip file from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
+ Unzip the file and within the file, you can run the command below to create the database schema
+ Keep the logAnalysis.py script within the newsdata folder to run

```
deploy@hopperTestRemote:~/logsAnalysis/newsdata$ sudo -u postgres psql -d news -f newsdata.sql 

deploy@hopperTestRemote:~/logsAnalysis/newsdata$ python logAnalysis.py

```

## Results

  + What are the most popular three articles of all time ?
  --------------------------------------------------------
  ```
  "Candidate is jerk, alleges rival" -- 338647 views
  "Bears love berries, alleges bear" -- 253801 views
  "Bad things gone, say good people" -- 170098 views
  ```
  
  + Who are the most popular article authors of all time ?
  --------------------------------------------------------
  ```
  Ursula La Multa -- 507594 views
  Rudolf von Treppenwitz -- 423457 views
  Anonymous Contributor -- 170098 views
  ```
  
  + On which days did more than 1% of requests lead to errors ?
  --------------------------------------------------------
  ```
  Jul 17, 2016 --  2.3% errors
  ```


## Helpful Links
+ https://linuxize.com/post/how-to-install-postgresql-on-debian-9/
