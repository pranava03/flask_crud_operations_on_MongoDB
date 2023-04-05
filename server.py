from flask import Flask, Response,request,jsonify
import pymongo
import json
from bson.objectid import ObjectId
from flask_restful import Resource, Api, abort, reqparse,fields, marshal_with
app = Flask(__name__)
api = Api(app)

 



class company(db.Document):
    _id = db.IntField(requried = True)
    name = db.StringField(requried = True)
    email = db.StringField(requried = True)
    pwd = db.StringField(requried = True)

details = {
    1 : {"name" : "write hello World Program", "email" : "write  the code using python.",
         "pwd" : "something alphanumeric"}
     }

name_post_args = reqparse.RequestParser()
name_post_args.add_argument("name", type=str, required=True)
name_post_args.add_argument("email", type=str, required=True)
name_post_args.add_argument("pwd", type=str, required=True)

name_put_args = reqparse.RequestParser()
name_put_args.add_argument("name", type=str)
name_put_args.add_argument("email", type=str)
name_put_args.add_argument("pwd", type=str)


resource_fields = {
    "_id" : fields.Integer,
    "name" :fields.String,
    "email":fields.String,
    "pwd":fields.String
}

class  empslist(Resource):
    def get(self):
        details = users.objects.get()
        details = {}
        for name in namess:
            details[name.id] = {"name" : name.name, "email" : name.email}
        return name   

class emp(Resource):
    @marshal_with(resource_fields)
    def get(self, detail_id):
        name = users.objects.get(_id = detail_id)
        if not name:
            abort(404, message = "Could not find task with that id")
        return name
    
    @marshal_with(resource_fields)
    def post(self, detail_id):
        args = name_post_args.parse_args()
        detail = users(_id=detail_id, name = args["name"], email = args["email"],pwd = args["pwd"]).save()
        id_ = detail_id
        return{"id" : str(id_)}, 201
    
    def delete(self, detail_id):
        users.objects.get(_id = detail_id).delete()
        return "task deleted!",204

    @marshal_with(resource_fields)
    def put(self, detail_id):
        args = name_put_args.parse_args()
        if args["name"]:
            users.objects.get(_id = detail_id).update(name = args["name"])
        if args["email"]:
            users.objects.get(_id = detail_id).update(email = args["email"])
        if args["pwd"]:
            users.objects.get(_id = detail_id).update(pwd = args["pwd"])
        return "{} updated!".format(detail_id),200


api.add_resource(emp, '/details/<int:detail_id>')
api.add_resource(empslist, '/details')


##############################
if __name__ == "__main__":
    app.run(port = 80, debug = True)