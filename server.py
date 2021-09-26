from flask import Flask,jsonify,request
from open_ai_call import openAiCall
app = Flask(__name__)

@app.route("/",methods=["POST"])
def api():
    obj=openAiCall(request.get_json())
    return obj.call_ai()


    
app.run(debug=True)