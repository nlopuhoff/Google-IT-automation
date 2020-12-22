#! /usr/bin/env python3

import os
import requests
import json

src = '/data/feedback/'
titles = ["title", "name", "date", "feedback"]

def dictionary_from_txt(file):
    dict = {}
    lst = []
    with open(src + file) as fle:
        for line in fle:
            words = line.split("\n")[:-1]
            for word in words:
                lst.append(word)

        for index in range(len(titles)):
            dict[titles[index]] = lst[index]
    return dict


for file in os.listdir (src):
    #print(dictionary_from_txt(file))
    response = requests.post("http://34.67.252.109/feedback/", data=dictionary_from_txt(file))
    print(response.status_code)

#################### + multiprocessing ##########################
#! /usr/bin/env python3

import requests
import os
from multiprocessing import Pool

srcDir = "/data/feedback/"
dataKeys = ['title', 'name', 'date', 'feedback']

def sender(filename):
	dataDict = {}
	with open(srcDir+filename, 'r') as fh:
		lines = fh.readlines()
		for k, v in zip(dataKeys, lines):
			dataDict.update({k: v})
	resp = requests.post("http://<corpweb-external-IP>/feedback/", json=dataDict)
	print(resp.raise_for_status())
	print(resp.status_code)

Files = os.listdir(srcDir)
Po = Pool(len(Files))
Po.map(sender, Files)
#################### short code ###################################

import os
import requests

IP_ADDR = '34.71.216.6'
feedbackDir = "/data/feedback/"
feedbackFiles = os.listdir(feedbackDir)
for f in feedbackFiles:
    fb = open(feedbackDir+f)
    data = fb.read().split("\n")
    dict = {"title":data[0], "name":data[1], "date":data[2], "fedback":data[3]}
    response = requests.post('http://{}/feedback'.format(IP_ADDR), json=dict)
    print(response.status_code)

################## short code #2 ##################################
feedback_dir = "/data/feedback/"
website_dir = "/projects/corpweb/"
url = "http://34.68.197.162/feedback/"
feedback_dic = {}

for feedback_file in os.listdir(feedback_dir):
    with open(feedback_dir + feedback_file,"r") as f:
        lines = f.readlines()
        feedback_dic["title"] = lines[0]
        feedback_dic["name"] = lines[1]
        feedback_dic["date"] = lines[2]
        feedback_dic["feedback"] = lines[3]
        response = requests.post(url, data=feedback_dic)
        print(response.status_code)
        print(response.ok)

################ using key_count instead of index ###################
#! /usr/bin/env python3

import os
import requests

# Path to the data
path = "/data/feedback/"

keys = ["title", "name", "date", "feedback"]

folder = os.listdir(path)
for file in folder:
    keycount = 0
    fb = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            fb[keys[keycount]] = value
            keycount += 1
    print(fb)
    response = requests.post("http://<IP Address>/feedback/",
    json=fb)
print(response.request.body)
print(response.status_code)

######################## short code ###############################
#! /usr/bin/env python3

import os
import requests

for file in os.listdir('/data/feedback/'):
 with open('/data/feedback/' + file) as f:
  data = {'title' : f.readline().rstrip('\n'), 'name' : f.readline().rstrip('\n'), 'date' : f.readline().rstrip('\n'), 'feedback' : f.read().rstrip('\n')}
  response = requests.post("http://35.193.177.195/feedback/", json = data)
  print(response.ok)
