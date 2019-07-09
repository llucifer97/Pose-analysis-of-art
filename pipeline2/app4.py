##get data of keypoints from mongodb


import json
import pymongo
from flask import Flask,request
from flask_restful import Resource, Api
from flask_restful import reqparse
from pymongo import MongoClient
from natsort import natsorted, ns
import sys
import os
import datetime

now = datetime.datetime.now()

app = Flask(__name__)
api = Api(app)
 v
cluster = MongoClient("mongodb+srv://ayush:1234@cluster0-tcwk1.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["gesture_data"]
collection = db["pose_pts"]




class keypoint(Resource):
    def get(self,_id):
        parser = reqparse.RequestParser()
        parser.add_argument('_id', type=str)
 #       parser.add_argument('user', type=str)

        data = parser.parse_args()

        results = collection.find({"_id":data['_id']})
        db_results = []
        for result in results:
            db_results.append(result)
        return db_results

class keypoints(Resource):

    def get(self):
        results = collection.find({})
        db_results = []
        for result in results:
            db_results.append(result)
        return db_results


api.add_resource(keypoint,'/pose/<path:_id>')
api.add_resource(keypoints,'/poses')

#if __name__ == '__main__':
app.run(port = 8080)












