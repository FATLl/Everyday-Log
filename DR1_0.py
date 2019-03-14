# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:41:16 2017
Project Daily record
@author: Frank
"""
filename='daily record.txt'

import datetime
now = datetime.datetime.now() 
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
with open(filename, 'a') as file_object:
    file_object.write('\n'+otherStyleTime)
print("Hello,Frank! Please enter your daily record:")
mesg=input()
with open(filename, 'a') as file_object:
    file_object.write('\n'+mesg)
while True:
    print('Anything else? No to end.')
    mesg2=input()
    if mesg2!='No':
        with open(filename, 'a') as file_object:
            file_object.write('\n'+mesg2)
    else:
        print('See you tommorow!')
        break
