
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def get_db():
    # Use a service account
    cred = credentials.Certificate('./serviceAccount/straightbody-4dec9-firebase-adminsdk-nawot-ce763cf334.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

def get_firebase():
    return firebase_admin