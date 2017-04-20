# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:41:16 2017
Project Daily record
@author: Administrator
"""
filename='daily record.txt'

import datetime
now = datetime.datetime.now() 
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
with open(filename, 'a') as file_object:
    file_object.write('\n'+otherStyleTime)
print("Hello,Frank")
mesg=input("Please enter your daily record:")
with open(filename, 'a') as file_object:
    file_object.write('\n'+mesg)
