from win10toast import ToastNotifier
import firebase_admin
import firebase_setup
from firebase_admin import credentials
from firebase_admin import firestore

def notify():
    db = firestore.client()
    Eye_ref = db.collection('EyeMovement')
    query = Eye_ref.order_by('time', direction=firestore.Query.DESCENDING).limit(1)
    results = query.stream()
    last_doc = list(results)[-1].to_dict()
    time_on = last_doc['time']

    counter = last_doc['contactCounter']
    time_counter = last_doc['counter']

    # One-time initialization
    toaster = ToastNotifier()
    if counter >= 4636:
        toaster.show_toast("Notification!", "You have been watching the screen for 40 minutes, take a 5-10 min break off screen", threaded=True,
                    icon_path=None, duration=3)  # 3 seconds

    # if counter >= 4636:
    #     toaster.show_toast("Notification!", "You have been watching the screen for 40 minutes, take a 5-10 min break off screen", threaded=True,
    #                    icon_path=None, duration=3)  # 3 seconds
    # Show notification whenever needed


    # To check if any notifications are active,
    # use `toaster.notification_active()`
    import time
    while toaster.notification_active():
        time.sleep(0.1)

def get_screentime():
    db = firestore.client()
    Eye_ref = db.collection('EyeMovement')
    query = Eye_ref.order_by('time', direction=firestore.Query.DESCENDING).limit(1)
    results = query.stream()
    last_doc = list(results)[-1].to_dict()
    return last_doc['counter']

def get_break():
    db = firestore.client()
    Eye_ref = db.collection('EyeMovement')
    query = Eye_ref.order_by('time', direction=firestore.Query.DESCENDING).limit(1)
    results = query.stream()
    last_doc = list(results)[-1].to_dict()
    return 4636 - last_doc['counter']