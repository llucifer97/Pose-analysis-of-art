import urllib.request
import re
import requests
import urllib
import os
from urlextract import URLExtract
try:
    os.mkdir('images')
except FileExistsError as e :
    print("directory already exist")
with open("./urls") as file:
    for line in file:

        extractor = URLExtract()
        example_text = line

        for url in extractor.gen_urls(example_text):
            print(url)
            print("downloading image...")
            print(url.split('/')[-1])
            filename = url.split('/')[-1]
            urllib.request.urlretrieve(url, './images/' + filename)



