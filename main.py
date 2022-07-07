from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime, date, time
from json import dumps
import json

application = Flask(__name__)

dj = mysql.connector.connect(
    host='logindb1.cc4euyfhpe3u.us-east-1.rds.amazonaws.com',
    user='admin',
    password='dj756132',
    database='sys'
)
mycursor = dj.cursor()


# @application.route('/forschool', methods=['POST', 'GET'])
# def forschool():
#     global data_status

#     if request.method == 'POST':
#         data_status = {"responseStatus": 0, "results": ""}
#         firstname = request.json['firstname']
#         lastname = request.json['lastname']
#         reason = request.json['reason']
#         mobile = request.json['mobile']
#         date = datetime.now()
#         time = datetime.now()
#         mycursor.execute("insert into temporary_school values(%s,%s,%s,%s,%s,%s)",(firstname, lastname, reason, mobile, date, time))
#         dj.commit()
#         #mycursor.close()
#         data_status["responseStatus"] = 1
#         data_status["results"] = "success"
#         return data_status
#     else:
#         data_status["responseStatus"] = 0
#         data_status["result"] = "Required fields are missing"
#         return data_status


@application.route('/getschool', methods=['POST', 'GET'])
def getschool():
    global data_status
    global mycursor
    if request.method == 'GET':
        data_status = {"responseStatus": 0, "results": ""}
        mycursor.execute("select * from temporary_school")
        ab = mycursor.fetchall()
        l = []
        for i in ab:
            dic = {}
            #for j in i:
            dic["firstname"] = i[0]
            dic["lastname"] = i[1]
            dic["reason"] = i[2]
            dic["mobile"] = i[3]
            dic["date"] = i[4]
            ti = (datetime.min + i[5]).time()
            json_str = json.dumps({'created_at': ti}, default=str)
            dic["time"] = json_str
            l.append(dic)
        data_status["responseStatus"] = 1
        data_status["details"] = l
        data_status["results"] = "success"
        print(data_status)
        return jsonify(l)
    else:
        data_status["responseStatus"] = 0
        data_status["result"] = "Data not available"
        return data_status

if __name__ == "__main__":
    #application.run(debug=True)
    application.run(host='0.0.0.0', port=8080)
