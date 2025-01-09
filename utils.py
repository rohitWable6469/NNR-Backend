import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate(r"configs\nnrdb-2a971-firebase-adminsdk-sbwoz-d95107b82f.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

def add_user(data):
    # Add data to Firestore
    doc_ref = db.collection("users").document()  # Auto-generate document ID
    doc_ref.set(data)
    print("User data added successfully!")
