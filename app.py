# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:48:31 2020

@author: PE20079451
"""
from flask import Flask, jsonify
from flask_restful import Resource, Api
import random
app=Flask(__name__)
api=Api(app)
class Student(Resource):
    def get(self, name):
        return {"student": name}
api.add_resource(Student, "/<string:name>")
@app.route("/createotp/<string:name>",methods=["GET"])
def four(name):
    z=""
    for x in name:
        y=str(random.randrange(0,9))
        z=z+x+y
        passwd=z.upper()
    return jsonify({"Password":passwd})

app.run(port=5000)