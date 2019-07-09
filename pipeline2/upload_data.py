# upload the generated keypoints to mongo db

import json
import pymongo
from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from pymongo import MongoClient
from natsort import natsorted, ns
import sys
import os
import datetime

# app = Flask(__name__)
# api = Api(app)

# reading json file
# pose_doc = []

from glob import glob

# get the value of user

#with open("./ayush") as file:
#    content = json.load(file)
#   print(content)

#print(natsorted(list(content[0].items()))[1][1])

now = datetime.datetime.now()

path_to_json = 'api_json/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
json_data = list()
for json_file in json_files:
    json_file_path = os.path.join(path_to_json, json_file)
    with open(json_file_path, "r") as f:
        json_data.append(json.load(f))

cluster = MongoClient("mongodb+srv://ayush:1234@cluster0-tcwk1.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["gesture_data"]
collection = db["pose_pts"]

arr = []
results = collection.find({})
db_results = []
for result in results:
    db_results.append(result)
    arr.append(result["_id"])

# print(max(arr))


for i in range(len(json_files)):
    try:
        w = natsorted(list(natsorted(list(json_data[i].items()))[0][1][0].items()))[7][1]

    except IndexError as e:
        print("no pose detected!")
        pass
    post1 = {
        "pose": json_data[i],
        "_id": i,  # remove max(arr) in case of any descrepancies
        "date": str(now),
 #       "user": natsorted(list(content[0].items()))[2][1],
        "file": str(json_files[i].split(".")[0])
#        "url":str(natsorted(list(content[0].items()))[1][1])

    }

    try:
        collection.insert_one(post1)
    except pymongo.errors.DuplicateKeyError:
        pass












