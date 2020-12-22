#!/usr/bin/env python3

import os
from PIL import Image
import requests

src = "/home/alex/TTest/images/"  # for *nix systems
dist = "/home/alex/TTest/images/" # for *nix systems
#counter = 0

for img in os.listdir(src):
    if "tiff" in img:
        #counter += 1
        im = Image.open(src + img)
        im.convert('RGB').resize((600,400)).save(dist + img.split(".tiff")[0] + ".jpeg", "JPEG") # that doesnt work properly: "00{}".format(counter)
