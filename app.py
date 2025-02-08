from flask import Flask, request, jsonify
import os
import firebase_admin
from firebase_admin import credentials, firestore
import json
from flask_cors import CORS  # Import CORS
import time
from datetime import datetime
import random
import string


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


def generate_customer_id(length=8):
    customer_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return customer_id


def add_user(data):
    # Add data to Firestore
    doc_ref = db.collection("users").document()  # Auto-generate document ID
    doc_ref.set(data)
    print("User data added successfully!")


def add_document(data):
    # Add data to Firestore
    doc_ref = db.collection("documents").document()  # Auto-generate document ID
    doc_ref.set(data)
    print("Documents data added successfully!")


def add_ae_document(data, key):
    # Add data to Firestore
    doc_ref = db.collection(key).document()  # Auto-generate document ID
    doc_ref.set(data)
    print(f"{key} data added successfully in Avantika Enterprises!")
    

# def add_ae_customer(data):
#     # Add data to Firestore
#     doc_ref = db.collection("ae_customers").document()  # Auto-generate document ID
#     doc_ref.set(data)
#     print("Documents data added successfully!")


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


@app.route('/submit_document', methods=['POST'])
def submit_document():
    try:
        # Get form data from the request
        data = request.json
        # Get the current time in seconds since the Unix epoch
        current_time_seconds = time.time()

        # Convert to a readable date and time format
        readable_time = datetime.fromtimestamp(current_time_seconds).strftime('%d-%m-%Y %H:%M:%S')
        data["timestamp"] = readable_time
        add_document(data)
        return jsonify({"message": "Document added successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to add data'}), 500


@app.route('/get_all_documents', methods=['GET'])
def get_all_documents():
    try:
        # Fetch all documents from the "documents" collection
        documents_ref = db.collection('documents')
        docs = documents_ref.stream()

        # Prepare the response list
        documents = []
        for doc in docs:
            document_data = doc.to_dict()
            document_data['id'] = doc.id  # Include the document ID
            documents.append(document_data)

        return jsonify(documents), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to fetch documents'}), 500


@app.route('/ae/submit_document', methods=['POST'])
def submit_ae_document():
    try:
        # Get form data from the request
        data = request.json
        # Get the current time in seconds since the Unix epoch
        current_time_seconds = time.time()

        # Convert to a readable date and time format
        readable_time = datetime.fromtimestamp(current_time_seconds).strftime('%d-%m-%Y %H:%M:%S')
        data["timestamp"] = readable_time
        add_ae_document(data, 'ae_documents')
        return jsonify({"message": "Document added successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to add data'}), 500


@app.route('/ae/get_all_documents', methods=['GET'])
def get_all_ae_documents():
    try:
        # Fetch all documents from the "documents" collection
        documents_ref = db.collection('ae_documents')
        docs = documents_ref.stream()

        # Prepare the response list
        documents = []
        for doc in docs:
            document_data = doc.to_dict()
            document_data['id'] = doc.id  # Include the document ID
            documents.append(document_data)

        return jsonify(documents), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to fetch documents'}), 500


@app.route('/ae/submit_customer', methods=['POST'])
def submit_ae_new_customer():
    try:
        # Get form data from the request
        data = request.json
        # Get the current time in seconds since the Unix epoch
        current_time_seconds = time.time()

        # Convert to a readable date and time format
        readable_time = datetime.fromtimestamp(current_time_seconds).strftime('%d-%m-%Y %H:%M:%S')
        data["customerId"] = generate_customer_id()
        data["timestamp"] = readable_time
        add_ae_document(data, 'ae_customers')
        return jsonify({"message": "Document added successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to add data'}), 500


@app.route('/ae/get_all_customers', methods=['GET'])
def get_all_ae_customers():
    try:
        # Fetch all documents from the "documents" collection
        documents_ref = db.collection('ae_customers')
        docs = documents_ref.stream()

        # Prepare the response list
        documents = []
        for doc in docs:
            document_data = doc.to_dict()
            document_data['id'] = doc.id  # Include the document ID
            documents.append(document_data)

        return jsonify(documents), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to fetch documents'}), 500


@app.route('/ae/submit_expense', methods=['POST'])
def submit_ae_new_expense():
    try:
        # Get form data from the request
        data = request.json
        # Get the current time in seconds since the Unix epoch
        current_time_seconds = time.time()

        # Convert to a readable date and time format
        readable_time = datetime.fromtimestamp(current_time_seconds).strftime('%d-%m-%Y %H:%M:%S')
        data["expenseId"] = generate_customer_id()
        data["timestamp"] = readable_time
        add_ae_document(data, 'ae_expenses')
        return jsonify({"message": "Expense added successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to add data'}), 500


@app.route('/ae/get_all_expenses', methods=['GET'])
def get_all_ae_expenses():
    try:
        # Fetch all documents from the "documents" collection
        documents_ref = db.collection('ae_expenses')
        docs = documents_ref.stream()

        # Prepare the response list
        documents = []
        for doc in docs:
            document_data = doc.to_dict()
            document_data['id'] = doc.id  # Include the document ID
            documents.append(document_data)

        return jsonify(documents), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to fetch documents'}), 500


@app.route('/ae/submit_payment', methods=['POST'])
def submit_ae_new_payment():
    try:
        # Get form data from the request
        data = request.json
        # Get the current time in seconds since the Unix epoch
        current_time_seconds = time.time()

        # Convert to a readable date and time format
        readable_time = datetime.fromtimestamp(current_time_seconds).strftime('%d-%m-%Y %H:%M:%S')
        data["expenseId"] = generate_customer_id()
        data["timestamp"] = readable_time
        add_ae_document(data, 'ae_payment')
        return jsonify({"message": "Payment added successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to add data'}), 500


@app.route('/ae/get_all_payments', methods=['GET'])
def get_all_ae_payments():
    try:
        # Fetch all documents from the "documents" collection
        documents_ref = db.collection('ae_payment')
        docs = documents_ref.stream()

        # Prepare the response list
        documents = []
        for doc in docs:
            document_data = doc.to_dict()
            document_data['id'] = doc.id  # Include the document ID
            documents.append(document_data)

        return jsonify(documents), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to fetch documents'}), 500


@app.route('/ae/get_customers_stats', methods=['GET'])
def get_customer_stats():
    try:

        output = []

        # Fetch all Payment documents from the "documents" collection
        documents_ref = db.collection('ae_payment')
        payments_docs = documents_ref.stream()

        # Prepare the payment list
        payments = []
        for doc in payments_docs:
            document_data = doc.to_dict()
            document_data['id'] = doc.id  # Include the document ID
            payments.append(document_data)

        # Fetch all Invoice documents from the "documents" collection
        documents_ref = db.collection('ae_documents')
        invoice_docs = documents_ref.stream()

        # Prepare the invoice list
        invoices = []
        for doc in invoice_docs:
            document_data = doc.to_dict()
            document_data['id'] = doc.id  # Include the document ID
            invoices.append(document_data)

        # Fetch all Invoice documents from the "documents" collection
        documents_ref = db.collection('ae_documents')
        customer_docs = documents_ref.stream()

        # Prepare the invoice list
        customers = []
        for doc in customer_docs:
            document_data = doc.to_dict()
            document_data['id'] = doc.id  # Include the document ID
            customers.append(document_data)

        output = customer_stats_utils(customers, invoices, payments)



        return jsonify(output), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to fetch documents'}), 500


if __name__ == '__main__':
    app.run(debug=True)
