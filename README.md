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
unset PGURL
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

The shell commands to run csv2db.py are listed below:

```bash
cd ~/tkrapi20
. env.bash
bin/rmbad_cookies.bash
~/anaconda3/bin/python py/csv2db.py
```

I ran the above script on my laptop and it finished in about 30 seconds.

The script rmbad_cookies.bash removes CSV files which contain error messages from Yahoo rather than good data.

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

I ran the above script on my laptop and it finished after 5 minutes.
I used the Postgres psql command to see the features inside the features table:

```sql
ann@ub16aug:~/tkrapi20/py$ cd ..
ann@ub16aug:~/tkrapi20$ bin/psql.bash 
psql (9.5.8)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

tkrapi=# \d features
        Table "public.features"
 Column |       Type        | Modifiers 
--------+-------------------+-----------
 tkr    | character varying | 
 csv    | text              | 

tkrapi=# select count(tkr) from features;
 count 
-------
   711
(1 row)

tkrapi=# select tkr from features where tkr = '^GSPC';
  tkr  
-------
 ^GSPC
(1 row)

tkrapi=# select tkr, length(csv) from features where tkr = '^GSPC';
  tkr  | length  
-------+---------
 ^GSPC | 1840709
(1 row)

tkrapi=# select tkr, substring(csv for 256) from features where tkr = '^GSPC';
  tkr  |                                                   substring                                                    
-------+----------------------------------------------------------------------------------------------------------------
 ^GSPC | cdate,cp,pct_lead,pct_lag1,pct_lag2,pct_lag4,pct_lag8,slope3,slope4,slope5,slope6,slope7,slope8,slope9,dow,moy+
       | 1950-01-03,16.660,1.140,0.000,0.000,0.000,0.000,,,,,,,,0.020,0.010                                            +
       | 1950-01-04,16.850,0.475,1.140,0.000,0.000,0.000,,,,,,,,0.030,0.010                                            +
       | 1950-01-05,
(1 row)

tkrapi=# \q
ann@ub16aug:~/tkrapi20$
ann@ub16aug:~/tkrapi20$
ann@ub16aug:~/tkrapi20$
```

# Learn, Predict

After the features are ready, I can learn and predict from them.

A demonstration of the Python API which supports both Learn and Predict is listed below:

```python
cd ~/tkrapi20
~/anaconda3/bin/python
import kerastkr
kerastkr.learn_predict_kerasnn('^GSPC',25,'2017-08')
```

The above syntax should predict one-day percent gain, a variable I call: 'pct_lead', for each day in the month 2017-08.

The predictions are for a ticker called: '^GSPC' which tracks the S&P 500 index.

The Keras model which calculates the predictions learns from 25 years of ^GSPC features (created from dates and prices).

I ran the above syntax on my laptop and captured a screenshot:

```python
ann@ub16aug:~$ 
ann@ub16aug:~$ cd ~/tkrapi20


ann@ub16aug:~/tkrapi20$ . env.bash


ann@ub16aug:~/tkrapi20$ ~/anaconda3/bin/python
Python 3.6.1 |Anaconda custom (64-bit)| (default, May 11 2017, 13:09:58) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>


>>> import kerastkr
Using TensorFlow backend.



>>> kerastkr.learn_predict_kerasnn('^GSPC',25,'2017-08')
Epoch 1/1024
2017-08-24 14:17:04.077248: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
2017-08-24 14:17:04.077279: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-08-24 14:17:04.077288: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
6301/6301 [==============================] - 0s - loss: 2.3986     
Epoch 2/1024
6301/6301 [==============================] - 0s - loss: 1.8951

SNIP...

Epoch 1023/1024
6301/6301 [==============================] - 0s - loss: 1.2835     
Epoch 1024/1024
6301/6301 [==============================] - 0s - loss: 1.2787     
            cdate       cp  pct_lead  prediction  effectiveness  accuracy
17004  2017-08-01  2476.35     0.049       0.029          0.049       1.0
17005  2017-08-02  2477.57    -0.218       0.034         -0.218       0.0
17006  2017-08-03  2472.16     0.189       0.046          0.189       1.0
17007  2017-08-04  2476.83     0.165       0.024          0.165       1.0
17008  2017-08-07  2480.91    -0.241       0.027         -0.241       0.0
17009  2017-08-08  2474.92    -0.036       0.050         -0.036       0.0
17010  2017-08-09  2474.02    -1.447       0.037         -1.447       0.0
17011  2017-08-10  2438.21     0.128       0.131          0.128       1.0
17012  2017-08-11  2441.32     1.004       0.067          1.004       1.0
17013  2017-08-14  2465.84    -0.050       0.004         -0.050       0.0
17014  2017-08-15  2464.61     0.142       0.048          0.142       1.0
17015  2017-08-16  2468.11    -1.544       0.005         -1.544       0.0
17016  2017-08-17  2430.01    -0.184       0.111         -0.184       0.0
17017  2017-08-18  2425.55     0.116       0.081          0.116       1.0
17018  2017-08-21  2428.37     0.994       0.065          0.994       1.0
17019  2017-08-22  2452.51    -0.345       0.011         -0.345       0.0
17020  2017-08-23  2444.04     0.000       0.039          0.000       0.5
>>> quit()
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$
```

The above tabular report is output from a Pandas DataFrame.

In a middle column I see the predictions from my Keras model.

In this example all of the predictions are above zero so they are bullish predictions.

The most bullish prediction was issued for 2017-08-10.

When I look to the right of that prediction I see it was an accurate predicition.

I consider any prediction which can predict the sign of pct_lead, to be an accurate prediction.

Lets attach this Python syntax to a FlaskRESTful API server.

# FlaskRESTful

I use the syntax below to start the FlaskRESTful API server:

```bash
cd ~/tkrapi20
./flaskr.bash
```

I ran the above syntax on my laptop and captured a screenshot:

```bash
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$ ./flaskr.bash 
Using TensorFlow backend.
 * Running on http://0.0.0.0:5011/ (Press CTRL+C to quit)
 * Restarting with stat
Using TensorFlow backend.
 * Debugger is active!
 * Debugger PIN: 167-686-399
```

So, that shell became locked.

I started another shell and issued a simple curl command.

I captured a screenshot:

```json
ann@ub16aug:~/tkrapi20$ curl localhost:5011/demos
{
    "demos": [
        "/demos",
        "/algo_demos",
        "/features",
        "/tkrs",
        "/tkrlist",
        "/years",
        "/tkrinfo/IBM",
        "/tkrprices/SNAP",
        "/istkr/YHOO",
        "/demo11.json",
        "/static/hello.json",
        {
            "algo_demos": [
                "/sklinear/IBM/20/2017-08/'pct_lag1,slope3,dow,moy'",
                "/sklinear_yr/IBM/20/2016/'pct_lag1,slope3,dow,moy'",
                "/sklinear_tkr/IBM/20/'pct_lag1,slope3,dow,moy'",
                "/keraslinear/FB/3/2017-08/'pct_lag2,slope5,moy'",
                "/keraslinear_yr/IBM/20/2016/'pct_lag1,slope3,dow,moy'",
                "/keraslinear_tkr/IBM/20/'pct_lag1,slope3,dow,moy'",
                "/keras_nn/FB/3/2017-07?features='pct_lag1,slope4,moy'&hl=2&neurons=4",
                "/keras_nn_yr/FB/3/2017?features='pct_lag1,slope4,moy'&hl=2&neurons=4",
                "/keras_nn_tkr/FB/3?features='pct_lag1,slope4,moy'&hl=2&neurons=4"
            ],
            "features": [
                "pct_lag1",
                "pct_lag2",
                "pct_lag4",
                "pct_lag8",
                "slope3",
                "slope4",
                "slope5",
                "slope6",
                "slope7",
                "slope8",
                "slope9",
                "dow",
                "moy"
            ]
        }
    ]
}
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$
```

Also I noticed that FlaskRESTful added a line to its shell:

```bash
ann@ub16aug:~/tkrapi20$ ./flaskr.bash 
Using TensorFlow backend.
 * Running on http://0.0.0.0:5011/ (Press CTRL+C to quit)
 * Restarting with stat
Using TensorFlow backend.
 * Debugger is active!
 * Debugger PIN: 167-686-399
127.0.0.1 - - [24/Aug/2017 14:51:54] "GET /demos HTTP/1.1" 200 -
```

The above output tells me that FlaskRESTful saw a GET request for /demos and the response code was 200 which usually means good news.

Remember above that I had asked for a month of predictions using Python syntax:

```python
kerastkr.learn_predict_kerasnn('^GSPC',25,'2017-08')
```

I sent a similar request to FlaskRESTful using curl and captured a screenshot:

```json
ann@ub16aug:~/tkrapi20$ curl localhost:5011"/keras_nn/^GSPC/25/2017-08?features='pct_lag1,slope4,moy'&hl=2&neurons=4"
{
    "predictions": {
        "Long-Only-Accuracy": 0.5,
        "Long-Only-Effectivness": -1.278,
        "Model-Effectivness": -1.278,
        "Model-Accuracy": 0.5,
        "Prediction-Count": 17,
        "Prediction-Details": [
            {
                "date,price": [
                    "2017-08-01",
                    2476.35
                ],
                "pct_lead": 0.049,
                "prediction,effectiveness,accuracy": [
                    0.032999999821186066,
                    0.049,
                    1.0
                ]
            },
            {
                "date,price": [
                    "2017-08-02",
                    2477.57
                ],
                "pct_lead": -0.218,
                "prediction,effectiveness,accuracy": [
                    0.03700000047683716,
                    -0.218,
                    0.0
                ]
            },
            {
                "date,price": [
                    "2017-08-03",
                    2472.16
                ],
                "pct_lead": 0.18899999999999997,
                "prediction,effectiveness,accuracy": [
                    0.04800000041723251,
                    0.18899999999999997,
                    1.0
                ]
            },
            {
                "date,price": [
                    "2017-08-04",
                    2476.83
                ],
                "pct_lead": 0.165,
                "prediction,effectiveness,accuracy": [
                    0.02800000086426735,
                    0.165,
                    1.0
                ]
            },
            {
                "date,price": [
                    "2017-08-07",
                    2480.91
                ],
                "pct_lead": -0.24100000000000002,
                "prediction,effectiveness,accuracy": [
                    0.03099999949336052,
                    -0.24100000000000002,
                    0.0
                ]
            },
            {
                "date,price": [
                    "2017-08-08",
                    2474.92
                ],
                "pct_lead": -0.036000000000000004,
                "prediction,effectiveness,accuracy": [
                    0.050999999046325684,
                    -0.036000000000000004,
                    0.0
                ]
            },
            {
                "date,price": [
                    "2017-08-09",
                    2474.02
                ],
                "pct_lead": -1.4469999999999998,
                "prediction,effectiveness,accuracy": [
                    0.03999999910593033,
                    -1.4469999999999998,
                    0.0
                ]
            },
            {
                "date,price": [
                    "2017-08-10",
                    2438.21
                ],
                "pct_lead": 0.128,
                "prediction,effectiveness,accuracy": [
                    0.12200000137090683,
                    0.128,
                    1.0
                ]
            },
            {
                "date,price": [
                    "2017-08-11",
                    2441.32
                ],
                "pct_lead": 1.004,
                "prediction,effectiveness,accuracy": [
                    0.06700000166893005,
                    1.004,
                    1.0
                ]
            },
            {
                "date,price": [
                    "2017-08-14",
                    2465.84
                ],
                "pct_lead": -0.05,
                "prediction,effectiveness,accuracy": [
                    0.012000000104308128,
                    -0.05,
                    0.0
                ]
            },
            {
                "date,price": [
                    "2017-08-15",
                    2464.61
                ],
                "pct_lead": 0.142,
                "prediction,effectiveness,accuracy": [
                    0.04899999871850014,
                    0.142,
                    1.0
                ]
            },
            {
                "date,price": [
                    "2017-08-16",
                    2468.11
                ],
                "pct_lead": -1.544,
                "prediction,effectiveness,accuracy": [
                    0.010999999940395355,
                    -1.544,
                    0.0
                ]
            },
            {
                "date,price": [
                    "2017-08-17",
                    2430.01
                ],
                "pct_lead": -0.184,
                "prediction,effectiveness,accuracy": [
                    0.10300000011920929,
                    -0.184,
                    0.0
                ]
            },
            {
                "date,price": [
                    "2017-08-18",
                    2425.55
                ],
                "pct_lead": 0.11599999999999999,
                "prediction,effectiveness,accuracy": [
                    0.07900000363588333,
                    0.11599999999999999,
                    1.0
                ]
            },
            {
                "date,price": [
                    "2017-08-21",
                    2428.37
                ],
                "pct_lead": 0.9940000000000001,
                "prediction,effectiveness,accuracy": [
                    0.06499999761581421,
                    0.9940000000000001,
                    1.0
                ]
            },
            {
                "date,price": [
                    "2017-08-22",
                    2452.51
                ],
                "pct_lead": -0.345,
                "prediction,effectiveness,accuracy": [
                    0.017999999225139618,
                    -0.345,
                    0.0
                ]
            },
            {
                "date,price": [
                    "2017-08-23",
                    2444.04
                ],
                "pct_lead": 0.0,
                "prediction,effectiveness,accuracy": [
                    0.04100000113248825,
                    0.0,
                    0.5
                ]
            }
        ]
    }
}
ann@ub16aug:~/tkrapi20$ 
ann@ub16aug:~/tkrapi20$ 
```

Also I noticed that FlaskRESTful added many lines to its shell:

```bash
Epoch 1/1024
6301/6301 [==============================] - 0s - loss: 1.3696     
Epoch 2/1024
6301/6301 [==============================] - 0s - loss: 1.3760     
Epoch 3/1024
6301/6301 [==============================] - 0s - loss: 1.3214     

SNIP ....

6301/6301 [==============================] - 0s - loss: 1.2838     
Epoch 1024/1024
6301/6301 [==============================] - 0s - loss: 1.2814     
127.0.0.1 - - [24/Aug/2017 15:03:45] "GET /keras_nn/^GSPC/25/2017-08?features='pct_lag1,slope4,moy'&hl=2&neurons=4 HTTP/1.1" 200 -
```

Next, I tried calling a different algorithm for a different ticker and different features, but same month:

```json

```
