from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route("/",methods=["POST"])
def hello():
    return request.get_json()


    
app.run(debug=True)