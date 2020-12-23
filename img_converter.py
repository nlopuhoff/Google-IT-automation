#!/usr/bin/env python3

import os
from PIL import Image
from multiprocessing import Pool
import multiprocessing

src = r'''C:/Users/OMEN/Desktop/images/''' #for WINDOWS
dist = r'''C:/Users/OMEN/Desktop/TTest/''' #for WINDOWS

#src = "/home/alex/images/"  # for *nix systems
#dist = "/home/alex/TTest/"  # for *nix systems

if not os.path.exists(dist):
    os.mkdir(dist)


def run(img):
    if not img.startswith("scr") and not img.startswith("."):
        im = Image.open(src + img)
        im.convert('RGB').rotate(270).resize((128,128)).save(dist + img + ".jpg", "JPEG")


if __name__ == "__main__" :

    #for img in os.listdir(src): #works without multiprocessing
        #run(img)

    list_ofimages = os.listdir(src) # because multiprocessing works only with lists
    p = Pool(multiprocessing.cpu_count())
    p.map(run, list_ofimages)
