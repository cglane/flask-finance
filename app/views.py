
from models import Columns,FileProfile,User
from app import app
from lib import predict
from flask import render_template, jsonify, request
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename
import os

def buildProfile(request,user_id):
    filePath = request.json['filePath']
    source = request.json['source']
    header = request.json['header']
    columns = request.json['columns']
    columns = Columns(date=columns['date'],
                    location=columns['location'],
                    value=columns['value'],
                    description=columns['description'])
    finances = FileProfile(filePath=filePath,
                        source=source,
                        header=header,
                        columns=columns)
    return finances

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home',
                           user=user)
@app.route('/api/user',methods=['POST','PUT'])
def user():
    username = request.json['username']
    password = request.json['password']
    updatedUser = User.objects(username=username).update_one(set__password=password, upsert=True)
    return jsonify({'result':updatedUser})

@app.route('/api/login',methods = ['POST','PUT'])
def login():
    username = request.json['username']
    password = request.json['password']
    myUser = User.objects(username=username,password=password)
    if myUser:
        print myUser[0].id
        return jsonify({'_id':str(myUser[0].id)})
    else:
        return jsonify({'result':'Wrong information'}),202
@app.route('/api/save_finances/<user_id>',methods = ['POST','PUT'])
def finances(user_id):
    user = User.objects(id=user_id).first()
    user.finances = buildProfile(request,user_id)
    user.save()
    return jsonify({'result':'success'})

@app.route('/api/save_amex/<user_id>',methods=['POST','PUT'])
def amex(user_id):
    user = User.objects(id=user_id).first()
    user.amex = buildProfile(request,user_id)
    user.save()
    return jsonify({'result':'success'})
@app.route('/api/read_user_profiles/<user_id>/<source>',methods=['GET'])
def readFiles(user_id,source):
    user = User.objects(id=user_id).first()
    if source == 'finances':
        transactions = user[source]
        readResponse = predict.readFinances(transactions)
    else:
        transactions = user[source]
        readResponse = predict.readCreditCard(transactions)
    return jsonify({"result":readResponse})
@app.route('/api/describe_transactions/<user_id>/<source>',methods=['POST'])
def describeTransactions(user_id,source):
    outputName = request.json['outputName']
    user = User.objects(id=user_id).first()
    finances = user.finances
    creditCard = user[source]
    outputName = predict.makePredictions(finances,creditCard,outputName)
    return jsonify({'filePath':outputName})
