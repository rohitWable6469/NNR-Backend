from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials,firestore


app = Flask(__name__)


cred = credentials.Certificate(r"configs\nnrdb-2a971-firebase-adminsdk-sbwoz-d95107b82f.json")
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
        add_user(data)
        return jsonify({"message": "User added successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to add data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
