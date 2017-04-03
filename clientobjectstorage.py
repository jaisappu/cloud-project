#!/usr/bin/python
import commands
commands.getstatusoutput('mkdir /media/jjd')
commands.getstatusoutput('mount 192.168.122.1:/server/jjd /media/jjd')
