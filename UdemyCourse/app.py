from flask import Flask
from flask import jsonify,request
from flask_restful import Api,Resource

app = Flask(__name__)
api=Api(app)

#define our resources

class Add(Resource):
    def post(self):
        #if i am here, then the resource add was requested using the method POST
        #Step 1 : get posted data 
        postedData = request.get_json()
        a= postedData["a"]
        b=postedData["b"]
        a=int(a)
        b=int(b)

        ret=a+b
        retMap={
            'Sum':ret,
            'Status Code':200
        }
        return jsonify(retMap)


class Subtract(Resource):
    pass 

class Multiply(Resource):
    pass 

class Divide(Resource):
    pass


# mapping resources 
api.add_resource(Add,"/add")
#flask(hi) we could add anything here

"""
    different datatypes we can send in json 
    {
    }
    {
    "field":3,
    "field":"abc",
    "boolean":1,
    "array":[1,2,3,4, "abc"],
    "array of objects":[
    {
        "field":1
    },
    {
        "field2":"this is a string"
    }

    ],


    "array of nested arrays":[
        "nested array":[
        {
            "field1":1, 
            "name":"Elfarouk"
        }
        ]
        }"""




@app.route("/")
#once this application is running it is always waiting for server to write 
# once they get the request at slash . Make this function handle a request 
# and handle ehe response 




def hello_world():
    return "hello world"



"""@app.route("/hello")
def hello():
    return "I just hit/hello"
"""
"""@app.route("/bye")

def bye():
    retJson={
            "Name":"Elfarouk",
            "Age":22, 
            "phones":[
                {
                    "phoneName":"Iphone8",
                },
            ]
        }


    return jsonify(retJson)"""
"""@app.route("/add_two_nums",methods=["POST"])

def add_two_nums():
    # Get x and y from the posted data 
    dataDict = request.get_json()
    if "y" not in dataDict:
        return "ERROR", 305
    a = dataDict["a"]
    b= dataDict["b"]

    c = a+b

    retJSON={
        "c":c
    }

    return jsonify(retJSON),200

    # Add z = x+y

    #Prepare a json  "z":z 

    # return json that we prepared 
"""

if __name__ == "__main__":

    #debug = true should be done only at testing and not at prdoction
    app.run(debug=True)

