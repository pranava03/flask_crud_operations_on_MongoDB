# flask_crud_operations_on_MongoDB(FCOOM):
This is a (python)flask oriented code,which performs the CRUD operations on the MongoDb database.
FCOOM is a basic flask framework containing of extensions many libraries, which is used as a base file by extending we can develop many more applications.

Set-Up To run The Application (Step by Step):
-> Make sure to install mongocompass before executing the program.
-> Open the zip folder in any text editor.
-> Import all the packages attached in the folder.
-> Open a terminal native to the machine.
-> Run the server by executing the program on the terminal
-> And perform all the crud operations on the mongodb.

For the successful execution of the program we used few in-built libraries of the 
Flask : Flask, Response,request,jsonify(libraries)
mongodb : pymongo(library)
bson : ObjectId(library)
json : json 

I also used few (hhtp//:) Request and Response methods for the communication of the data with database to that of the server run on localhost for the passing of aruguments manually by the user and the subsequent retrieval of the data for the desired query.
The HTTP Methods used in the program are:
GET,
PUT,
POST,
DELETE.
Also for these methods to pass the arguments we used few techniques
i.e : 
-> Passing of the argument through link request and response.
-> Passing through functions.(manually)
-> Specify the MIME type of the data with a Content-Type header   and so on...

To simplfiy the process i have created a few rest api's for the each of the CRUD operations:
-> Create user API
-> Reading a user API
-> Updating a user API
-> Delete a user API
-> Diplaying users by specifying an ID API

Developers:D.PranavaDatta
Project Duration: 31-3-2023 to 1-4-2023

Goal :

In this project, we aim to provide the simple use of the rest api's in contrast with flask . We will implement all the "CRUD" operations by usig flask on mongoDB with the help of api end points. This code  includes the path of  the rest api's and their implementation. We will go ahead with the existing libraries of the flask and mongodb, and that of the json. In the initial stages we can observer the successful connection of the virtual environment to the mongodb through a server which will run on the localhost native to the machine on which the code is being run and all the default Create, Read, Update, Delete operations on a database can be done by implementing a simple series of rest api end points in a virtual environment,which are capable of storing very huge data and the ability to retrive them,(to know the current functioning of an organisation.)

Technologies used:
Pymongo,
python,
mongo compass,
json, 
flask, 
Bson.

Running Requirements(libraries required):
Python 3.0.0,
virtual environment of python.
pymongo,
Flask,
Any text editor,
web server running on localhost,
postman.
