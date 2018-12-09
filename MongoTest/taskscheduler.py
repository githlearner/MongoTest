from flask import Flask,request,render_template,jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://127.0.0.1:27017")
db = client.Orchestrator
tasks = db.tasks


@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        res = request.form.to_dict()
        tasks.insert_one(res)
        displaydata = tasks.find()
        displaydata = [data for data in displaydata]
        return render_template("output.html",data=displaydata)
    return render_template('home.html')

@app.route('/wow')
def wowpage():
    return "SUCCESS REDIRECT"

if __name__ == '__main__':
    app.run(debug=True)

