# README.md

This repo, tkrapi20, should contain demos for a Meetup:

2017-08-24

Stock Market ML API with Flask-RESTful AND Keras-Tensor-Flow

https://www.meetup.com/BAyPIGgies/events/239118816/

https://www.meetup.com/Palo-Alto-Data-Science-Association/events/242451739/

The software in this repo was developed on Ubuntu 16.

If you want to run the demos on your laptop, you should install Ubuntu 16 on your laptop.

If you are on Mac or windows, a straightforward way to do this is to install VirtualBox.

After you install VirtualBox, download the file listed below and then import it into VirtualBox.

https://drive.google.com/file/d/0Bx3iDDAtxxI4VUtZcTRxTnZKZlk/

It is a large 10GB file.

After you import the above file, you should use the green-arrow in the VirtualBox GUI to boot Ubuntu 16.

After you boot Ubuntu 16, you should see a login screen for an account named: 'ann'.

The password is: 'a'

After I did the above steps, I logged in as 'ann' with password 'a'.

Next, I cloned this repo using a simple shell command:

```bash
cd ~ann
git clone https://github.com/danbikle/tkrapi20
```

I ran the first demo by issuing some shell commands:

```bash
cd ~ann
cd tkrapi20
. env.bash
python
```

I saw in the Python banner that I was running this:

```bash
ann@ub16aug:~/tkrapi20$ python
Python 3.6.1 |Anaconda 4.4.0 (64-bit)| (default, May 11 2017, 13:09:58) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
ann@ub16aug:~/tkrapi20$
```

The next demo I ran was a single shell command which is listed below:

```bash
conda install flask keras numpy pandas psycopg2 sqlalchemy
```

The above command finished after 90 seconds.

Next, I ran this shell command:

```bash
conda install flask-restful -c conda-forge
```

Then, I checked that the above packages were installed with shell commands:

```bash
conda list flask
conda list keras
conda list numpy
conda list pandas
conda list psycopg2
conda list sqlalchemy
```

Next, I worked with Postgres so this repo could interact with database tables.

I issued some shell commands:

```bash
sudo apt-get install postgresql postgresql-server-dev-all libpq-dev
sudo su - postgres
psql
```

At this point I was inside the psql interface which accepts both Postgres and SQL commands.

I typed three commands:

```sql
create database tkrapi;
create role tkrapi with login superuser password 'tkrapi';
\q
```

I typed exit at the shell prompt to exit the postgres Linux account and return to the ann account:

```bash
exit
```

In the py folder of this repo, I wrote some demos of packages:

* SQLAlchemy
* Keras
* FlaskRESTful

The shell commands for the first demo are listed below:

```bash
cd ~/tkrapi20/py
. ../env.bash
~/anaconda3/bin/python demosql.py
```

The above demo worked well so I stepped through the script with the pdb-debugger:

```bash
~/anaconda3/bin/python -m pdb demosql.py
```

The above demo worked well so I pointed demosql.py at a Postgres database on Heroku:

```bash
cd ~/tkrapi20/py
heroku create myapp2017abc
heroku addons:create heroku-postgresql:hobby-dev
heroku config
export PGURL='postgres://afizipm:33abc8@ec2-23-13-220-251.compute-1.amazonaws.com:5432/ddrpugf'
~/anaconda3/bin/python demosql.py
heroku pg:psql
select * from dropme;
\q
```

The above demo worked well so I ran some shell commands to start the Keras demo:

```bash
cd ~/tkrapi20/py
. ../env.bash
~/anaconda3/bin/python demokeras.py
```

The above demo worked well so I stepped through the script with the pdb-debugger:

```bash
~/anaconda3/bin/python -m pdb demokeras.py
```

The above demo worked well so I ran some shell commands to start the FlaskRESTful demo:

```bash
cd ~/tkrapi20/py
. ../env.bash
export PORT=5050
export FLASK_DEBUG=1
~/anaconda3/bin/python demoflask_restful.py
```

The above shell became locked. I call it Shell-1.

I started another shell, called Shell-2, and issued curl commands:

```bash
curl                            localhost:5050/hello.json
curl -d 'msg2flask=hello-flask' localhost:5050/hello.json
```

I saw this:

```bash
ann@ub16aug:~/tkrapi20/py$ curl http://0.0.0.0:5050/hello.json
{
    "hello": "world"
}
ann@ub16aug:~/tkrapi20/py$ 
ann@ub16aug:~/tkrapi20/py$ 
ann@ub16aug:~/tkrapi20/py$ 



ann@ub16aug:~/tkrapi20/py$ curl -d 'msg2flask=hello-flask' localhost:5050/hello.json
{
    "post-hello": "world",
    "curlmsg": "hello-flask"
}
ann@ub16aug:~/tkrapi20/py$ 
ann@ub16aug:~/tkrapi20/py$ 
ann@ub16aug:~/tkrapi20/py$ 
```

When I study the behavior of the above curl commands, I see that the get() method in demoflask_restful.py responds to the first curl command.

And I see that the post() method responds to the second.

These methods get() and post() correspond to HTTP verbs: GET, POST.

https://www.google.com/search?q=what+are+HTTP+verbs

So, that concludes the discussion about the three demos.

We have a sense of how the Python APIs work for SQLAlchemy, Keras, and FlaskRESTful.

Later we will blend the above three APIs into a simple API server.

But first we need to get some data.

# Get Data

I used shell commands listed below to get stock price data:

```bash
cd ~/tkrapi20
bin/request_tkr.bash
```

While the above command was running, I captured a partial screen shot:

```bash
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$ bin/request_tkr.bash
Thu Aug 24 00:11:38 PDT 2017
busy with ^GSPC
Wrote: /home/ann/tkrcsv/div/^GSPC.csv
Wrote: /home/ann/tkrcsv/history/^GSPC.csv
Wrote: /home/ann/tkrcsv/split/^GSPC.csv
busy with ^IXIC
Wrote: /home/ann/tkrcsv/div/^IXIC.csv
Wrote: /home/ann/tkrcsv/history/^IXIC.csv
Wrote: /home/ann/tkrcsv/split/^IXIC.csv
busy with ^RUT
Wrote: /home/ann/tkrcsv/div/^RUT.csv
Wrote: /home/ann/tkrcsv/history/^RUT.csv
Wrote: /home/ann/tkrcsv/split/^RUT.csv
busy with A
GET request of  A  failed. So I am trying again...
GET request of  A  failed. Maybe try later.
GET request of  A  failed. So I am trying again...
Wrote: /home/ann/tkrcsv/history/A.csv
GET request of  A  failed. So I am trying again...
Wrote: /home/ann/tkrcsv/split/A.csv
busy with AA
Wrote: /home/ann/tkrcsv/div/AA.csv
Wrote: /home/ann/tkrcsv/history/AA.csv
Wrote: /home/ann/tkrcsv/split/AA.csv
busy with AAL
Wrote: /home/ann/tkrcsv/div/AAL.csv
Wrote: /home/ann/tkrcsv/history/AAL.csv
Wrote: /home/ann/tkrcsv/split/AAL.csv
busy with AAP
Wrote: /home/ann/tkrcsv/div/AAP.csv
Wrote: /home/ann/tkrcsv/history/AAP.csv
Wrote: /home/ann/tkrcsv/split/AAP.csv
busy with AAPL
Wrote: /home/ann/tkrcsv/div/AAPL.csv
Wrote: /home/ann/tkrcsv/history/AAPL.csv
Wrote: /home/ann/tkrcsv/split/AAPL.csv
```

The above script needs between 5 and 6 hours to run.

I ran it on my laptop; after it finished I checked the disk usage:

```bash
ann@ub16aug:~/tkrapi20$ du -sh ~/tkrcsv/*
2.9M	/home/ann/tkrcsv/div
255M	/home/ann/tkrcsv/history
2.9M	/home/ann/tkrcsv/split
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$ 
```

The above script depends on tkrlist.txt, a list of 728 tickers, to declare which stocks to get.

If I am in a hurry, I update the script so it uses tkrlist_small.txt which lists these tickers:

```bash
ann@ub16aug:~/tkrapi20$ ll
total 104
drwxrwxr-x  7 ann ann  4096 Aug 24 00:11 .
drwxr-xr-x 41 ann ann  4096 Aug 24 00:10 ..
drwxrwxr-x  2 ann ann  4096 Aug 24 00:08 bin
-rw-rw-r--  1 ann ann   372 Aug 23 20:29 cr_tkrapi.sql
-rw-rw-r--  1 ann ann  5055 Aug 23 20:29 dev.py
-rw-rw-r--  1 ann ann   565 Aug 23 20:39 env.bash
-rw-rw-r--  1 ann ann  2685 Aug 23 21:04 features.txt
-rwxrwxr-x  1 ann ann   181 Aug 23 20:29 flaskr.bash
-rw-rw-r--  1 ann ann 10178 Aug 23 20:29 flaskr.py
drwxrwxr-x  8 ann ann  4096 Aug 24 00:08 .git
-rw-rw-r--  1 ann ann    12 Aug 23 20:29 .gitignore
-rw-rw-r--  1 ann ann  2218 Aug 23 20:29 meetup.txt
drwxrwxr-x  2 ann ann  4096 Aug 23 23:28 py
-rw-rw-r--  1 ann ann  5196 Aug 24 00:08 README.md
-rw-rw-r--  1 ann ann   713 Aug 23 20:29 README.old.md
-rw-rw-r--  1 ann ann    15 Aug 23 20:29 requirements.txt
-rw-rw-r--  1 ann ann    13 Aug 23 20:29 runtime.txt
drwxrwxr-x  2 ann ann  4096 Aug 23 20:29 static
drwxrwxr-x  2 ann ann  4096 Aug 23 20:29 tests
-rw-rw-r--  1 ann ann    70 Aug 23 20:29 tkrlist_small.txt
-rw-rw-r--  1 ann ann  3030 Aug 23 20:29 tkrlist.txt
-rw-rw-r--  1 ann ann    40 Aug 23 20:29 years.txt
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$ wc -l tkrlist.txt
728 tkrlist.txt
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$ cat tkrlist_small.txt 
^GSPC
^RUT
QQQ
DIA
GLD
TLT
AAPL
AMZN
BAC
FB
GOOG
JNJ
JPM
MSFT
WFC
XOM
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$
```

The script bin/request_tkr.bash, depends on py/request_tkr.py which depends on the Python requests package:

http://docs.python-requests.org

If you study request_tkr.py you will see it sends an initial request to a URL like this:

https://finance.yahoo.com/quote/IBM

Yahoo responds to that request with two pieces of information I need to track.

The first piece is in a browser cookie.

The second piece, I call it a crumb, is embedded within the HTML response from Yahoo.

The next request goes to a url like this:

https://finance.yahoo.com/quote/IBM/history?p=IBM

Then, another request goes to a url like this:

https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=-631123200&period2=1503561650&interval=1d&events=div&crumb=UCaZNLyqkGQ

Notice the crumb parameter at the end.

The Python script request_tkr.py figures out what that crumb should be by using a regexp search against a previous Yahoo HTML response.

If I send the wrong crumb (a crumb which fails to match my cookie), Yahoo responds with this friendly message:

```json
{
    "finance": {
        "error": {
            "code": "Unauthorized",
            "description": "Invalid cookie"
        }
    }
}
```

That is the only 'tricky' part of the script; the rest is plain-old web-scraping.

When Yahoo sees the above request, it usually responds with a CSV file after it matches the crumb with the cookie it had served me earlier.

I'm not sure why Yahoo is serving crumbs and cookies which frequently change but I thought that solving the puzzle was fun.

After the above script finishes, I run another script to copy all the CSV data into a Postgres table.

That script is named: csv2db.py

I should run csv2db.py after request_tkr.bash finishes.

The shell command to run csv2db.py is listed below:

```bash
cd ~/tkrapi20/py
. ../env.bash
~/anaconda3/bin/python csv2db.py
```

After I run csv2db.py, I am ready to generate machine learning features from dates and prices of each ticker.

# Generate Features

When I started working with stock market data many years ago I quickly saw that other people making decisions based on trendlines and candlesticks.

Also I saw some people making decisions based on what I call 'calendar events'.

For example some people like to sell in May and buy in October.

Or maybe they want to buy on Monday and sell on Friday.

I saw this behavior and used it to guide my efforts to create machine learning features from time series of prices.

The features I use in this repo are listed below:

* pct_lag1 (1 day pct pricelag)
* pct_lag2
* pct_lag4
* pct_lag8
* slope3 (normalized 3 day price moving avg slope)
* slope4
* slope5
* slope6
* slope7
* slope8
* slope9
* dow (integer day of week)
* moy (integer month of year)

Counting them up, we see that this repo has 13 features.

One feature I don't have but would like is daily interest rate.

The script which generates the above features from the CSV files is genf.py

The shell command to run genf.py is listed below

```bash
cd ~/tkrapi20/py
. ../env.bash
~/anaconda3/bin/python genf.py
```

# Learn, Predict

After the features are ready, I can learn and predict.

A demonstration of the Python API which supports both Learn and Predict is listed below:

```
cd ~/tkrapi20
python
import kerastkr
kerastkr.learn_predict_kerasnn('^GSPC',25,'2017-08')
```
