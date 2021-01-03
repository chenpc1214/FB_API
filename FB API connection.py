from flask import Flask,jsonify,request,render_template
from flask_restful import Api
#from merge_user_model import User,Users
#from merge_account import account_controller,one_controller
import pymysql
import traceback
import jwt                       #驗證系統(json_web_token)
import time
#from server import app           #從自建serve.py 引進 SQLAlchemy


app = Flask(__name__)
api = Api(app)                  #做一個api變數，引用python flask_restful中的套件 Api 函式

def index():
    return "Hello World"

@app.route('/') 
def index():
    return "Hello World"

@app.route('/login_test',methods=['GET'])
def login_test():
    return render_template('login_test.html')


@app.route('/login',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/modify_login',methods=['POST'])
def modify_login():
    userID=request.values['userID']
    accessToken = request.values['accessToken']
    print(userID,accessToken)
    return 'success'

if __name__ == "__main__":    
    app.debug = True          
    app.run(host = '127.0.0.1',ssl_context=('localhost+1.pem','localhost+1-key.pem')) 