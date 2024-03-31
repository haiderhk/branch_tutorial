from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

mongo_admin_user = os.getenv('MONGO_ADMIN_USER', 'default_user')
mongo_admin_pass = os.getenv('MONGO_ADMIN_PASS', 'default_pass')
db_name = os.getenv('MY_DB_NAME', 'default_db_name')

client = MongoClient(f'mongodb://{mongo_admin_user}:{mongo_admin_pass}@mongodb:27017/{db_name}?authSource=admin')
db = client[db_name]

@app.route('/')
def home():
    return "Welcome to the Home Page. For students page, go to /students"

@app.route('/students')
def get_students():
    try:
        students_collection = db['mlops_collection']
        students_cursor = students_collection.find()
        students_list = [{"Roll #": student["Roll#"], "Name": student["Name"]} for student in students_cursor]
        return jsonify({"Students": students_list})
    except Exception as e:
        return jsonify({"Error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)