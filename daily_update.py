# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:32:28 2019

@author: Andile XeroxZen
"""
import time

filename = 'daily_update.txt'
day_entry = input("What is the day's update? __ ")
today = time.ctime()

msg = day_entry + '\n Record of: {0}' .format(today)

with open(filename, 'a') as f:
    f.write(msg + '\n\n')