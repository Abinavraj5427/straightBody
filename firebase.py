
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    apiKey: "AIzaSyBzkhAV5Of1Nc2MYaBe9PIYL_MmuSq5URw",
    authDomain: "straightbody-4dec9.firebaseapp.com",
    databaseURL: "https://straightbody-4dec9.firebaseio.com/",
    projectId: "straightbody-4dec9",
    storageBucket: "straightbody-4dec9.appspot.com",
    messagingSenderId: "922824382292",
    appId: "1:922824382292:web:69586bb5eac68bf0c51ac1",
    measurementId: "G-C7RY3SJSX3"
})

db = firestore.client()