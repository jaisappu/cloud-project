#!/usr/bin/python2

import  cgi,cgitb
import  os,commands,time
from random import randint

cgitb.enable()

print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()

osn=x.getvalue('n')
rmm=x.getvalue('a')
cpu=x.getvalue('b')
h_size=x.getvalue('c')
portn=x.getvalue('e')
 
print "____________________________"

a=randint (7777 , 9999)

print commands.getstatusoutput('sudo virt-install --name '+osn+' --ram '+rmm+' --vcpu '+cpu+' --nodisk --cdrom /root/Downloads/kali-linux-2.0-amd64.iso  --graphics vnc,listen=0.0.0.0,port='+portn+'   --noautoconsole ')

print"/n"

print commands.getstatusoutput('sudo websockify -D '+str(a)+' 192.168.122.1:'+portn)

time.sleep(2)

print "plz wait for os "

print "Plese wait for launch !!"

print "<a href='http://192.168.122.1/noVNC/vnc.html?host=192.168.122.1&port="+str(a)+"'target='_blank'>click here to access your os</a>"





