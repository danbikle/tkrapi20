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
conda install keras flask sqlalchemy pandas numpy
```

The above command finished after 90 seconds.

Next, I ran this shell command:

```bash
conda install flask-restful -c conda-forge
```

Then, I checked that the above packages were installed:

```bash
conda list keras
conda list flask
conda list sqlalchemy
conda list pandas
conda list numpy
```