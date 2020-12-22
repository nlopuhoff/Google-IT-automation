#! /usr/bin/env python3

import requests
import os

src = "supplier-data/images/"
url = "http://localhost/upload/"

for img in os.listdir(src):
    if img.endswith("jpeg"):
        #print(img)
        with open(src + img, 'rb') as opened:
            r = requests.post(url, files = {'file': opened})
