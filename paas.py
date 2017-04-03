#!/usr/bin/python2

import cgi
import  cgitb
import  commands,os,time
from random import randint

cgitb.enable()

print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()

puser=data.getvalue('p')
a=randint(5555 , 6666)
if  puser == 'python':
        commands.getoutput('sudo docker run -itd -p ' + str(a)+':4200 py/start')
        print  "login as a start plz wait for python launch !!"
        print  "<a href='https://192.168.122.1:"+str(a)+"'>"
        print   "click here for python"
        print   "</a>"

elif  puser == 'ruby':
        commands.getoutput('sudo docker run -itd -p '+ str(a)+':4200 ruby/start')
        print  "login as a client plz wait for ruby !!"
        print  "<a href='https://192.168.122.1:"+str(a)+"'>"
        print   "click here for ruby"
        print   "</a>"

elif  puser == 'perl':
	commands.getoutput('sudo docker run -itd -p '+ str(a)+':4200 perl/start')
        print  "plz wait for perl !!"
        print  "<a href='https://192.168.122.1:"+str(a)+"'>"
        print   "click here for perl"
        print   "</a>"
        
else :
        print  "wrong choice !!"

