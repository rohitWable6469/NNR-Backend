from flask import Flask, request, jsonify
import os
import firebase_admin
from firebase_admin import credentials, firestore
import json
from flask_cors import CORS  # Import CORS
import time
from datetime import datetime

# Get the credentials from the environment variable
firebase_config = os.getenv('FIREBASE_CONFIG')
cred_dict = json.loads(firebase_config)
cred = credentials.Certificate(cred_dict)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# cred = credentials.Certificate(r"configs\nnrdb-2a971-firebase-adminsdk-sbwoz-d95107b82f.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

def add_user(data):
    # Add data to Firestore
    doc_ref = db.collection("users").document()  # Auto-generate document ID
    doc_ref.set(data)
    print("User data added successfully!")

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Get form data from the request
        data = request.json
        # Get the current time in seconds since the Unix epoch
        current_time_seconds = time.time()

        # Convert to a readable date and time format
        readable_time = datetime.fromtimestamp(current_time_seconds).strftime('%d-%m-%Y %H:%M:%S')
        data["timestamp"] = readable_time
        add_user(data)
        return jsonify({"message": "User added successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to add data'}), 500

@app.route('/', methods=['GET'])
def get_data():
    return jsonify({"message": "Welcome to NNR Application!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
