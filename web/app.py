from flask import Flask
from flask import jsonify,request
from flask_restful import Api,Resource

app = Flask(__name__)
api=Api(app)


def checkPostedData(postedData, functionName):
    if(functionName == "add" or functionName=="subtract" or functionName=="multiply"):
        if "a" not in postedData or "b" not in postedData:
            return 301 
        else:
            return 200
    elif functionName=="divide":
        if "a" not in postedData or "b" not in postedData:
            return 301 
        elif postedData["b"] == 0:
            return 302
        else:
            return 200

#define our resources
class Add(Resource):
    def post(self):
        #if i am here, then the resource add was requested using the method POST
        #Step 1 : get posted data 
        postedData = request.get_json()
        #Step 1b : Verify Validity of Posted Data
        status_code=checkPostedData(postedData)
        if(status_code!=200):
            retJSON={
                "Message":"An error happened",
                "Status Code": status_code

            }
            return jsonify(retJSON)
        #if we are here, then status_code =200
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
    def post(self):
        #if i am here, then the resource subtract was requested using the method POST

        #step1: Get posted data 
        postedData = request.get_json()

        #Step 1b = verfiy validity of posted data
        status_code = checkPostedData(postedData, "subtract")

        if(status_code!=200):
            retJson={
                "Message":"An error happend",
                "Status Code":status_code
            }
            return jsonify(retJson)
        a=postedData["a"]
        b=postedData["b"]
        a,b=int(a),int(b)
        ret=a-b
        retMap={
            'Difference':ret,
            'Status Code':200
        }
        return jsonify(retMap)


class Multiply(Resource):
    def post(self):
        postedData=request.get_json()
        status_code = checkPostedData(postedData, "multiply")
        if(status_code!=200):
            retJson={
                "Message":"An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        a=postedData["a"]
        b=postedData["b"]
        a,b=int(a),int(b)
        ret = a*b
        retMap={
            'Product':ret,
            'Status Code':200
        }
        return jsonify(retMap)
class Divide(Resource):
    def post(self):
        postedData=request.get_json()
        status_code = checkPostedData(postedData, "divide")
        if(status_code!=200):
            retJson={
                "Message":"An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)
        a=postedData['a']
        b=postedData['b']
        a,b = int(a),int(b)
        ret=a/b
        retMap={
            'Division':ret,
            'Status Code':200
        }
        return jsonify(retMap)



# mapping resources 
api.add_resource(Add,"/add")
api.add_resource(Subtract,"/subtract")
api.add_resource(Multiply,"/multiply")
api.add_resource(Divide,"/divide")
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

