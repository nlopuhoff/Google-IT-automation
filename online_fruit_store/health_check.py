#!/usr/bin/env python3

import shutil
import psutil
import emails
import os


sender = 'automation@example.com'
recipient = 'student-00-df7030d9be13@example.com'
body = 'Please check your system and resolve the issue as soon as possible.'
subject = ""


#Report an error if CPU usage is over 80%
CPU_usage = psutil.cpu_percent(1)
if CPU_usage > 79:
    subject += "Error - CPU usage is over 80%"
    emai = emails.generate(sender, recipient, subject, body, "")
    emails.send(emai)

#Report an error if available disk space is lower than 20%
disk_usage = psutil.disk_usage('/')[3] #total[0], used[1], free[2], percent[3]
if disk_usage > 79:
    subject += "Error - Available disk space is less than 20%"
    emai = emails.generate(sender, recipient, subject, body, "")
    emails.send(emai)

#Report an error if available memory is less than 500MB
free_memory = psutil.virtual_memory()[1]/1000000000
if free_memory < 0.501:
    subject += "Error - Available memory is less than 500MB"
    emai = emails.generate(sender, recipient, subject, body, "")
    emails.send(emai)

#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
hostname = "127.0.0.1"
response = os.system("ping -c 3 127.0.0.1") #if ping goes through, reponse == 0
if response != 0:
    subject += "Error - localhost cannot be resolved to 127.0.0.1"
    emai = emails.generate(sender, recipient, subject, body, "")
    emails.send(emai)
