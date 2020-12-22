#! /usr/bin/env python3

import os
import requests

linuxip = "http://localhost/fruits/" #"34.67.70.130"
feedbackDir = "supplier-data/descriptions/"

feedbackFiles = os.listdir(feedbackDir)
for txtfile in feedbackFiles:
    fb = open(feedbackDir+txtfile)
    data = fb.read().split("\n")
    #print(txtfile.split(".")[0])
    dict = {"name":data[0], "weight":int(data[1].split(" ")[0]), "description":data[2], "image_name":txtfile.split(".")[0]+".jpeg"}
    response = requests.post(linuxip, json=dict)
    print(response.status_code)
