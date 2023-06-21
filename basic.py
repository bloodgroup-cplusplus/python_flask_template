'''from flask import Flask 

app = Flask(__name__)

@app.route("/")
#127.0.0.1:5000


def index():
    return "<h1>Hello Puppy!</h1>"

@app.route("/information")

def info():
    return "<h1> Puppies are cute!</h1>"

@app.route('/puppy_name/<name>')

def puppylatin(name):
    #return "<h1>This is a page for {}</h1>".format(name.upper())
    if name[-1]!='y':
        return 'With y: {}'.format(name+'y')
    else:
        return "Replaced with iful:{}".format(name[:-1]+"iful")






if __name__ == "__main__":
    app.run(debug=True)'''


from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")

def index():
    name="Jose"
    letters=list(name)
    pup_dictionary={"pup_name":"Sammy"}
    return render_template("basic.html",name=name,letters=letters,pup_dictionary=pup_dictionary)


if __name__ =="__main__":
    app.run(debug=True)