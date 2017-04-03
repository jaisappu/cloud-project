#!/usr/bin/python 
import commands,os 
a=commands.getstatusoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.122.1 --discover') 
b=commands.getstatusoutput('iscsiadm --mode node --targetname rt --portal 192.168.122.1:3260 --login') 
print a 
print b 
