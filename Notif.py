from win10toast import ToastNotifier
import firebase_admin
import firebase_setup
from firebase_admin import credentials
from firebase_admin import firestore

db = firestore.client()
Eye_ref = db.collection('EyeMovement')
query = Eye_ref.order_by('time', direction=firestore.Query.DESCENDING).limit(1)
results = query.stream()
last_doc = list(results)[-1].to_dict()
time_on = last_doc['time']
print(time_on)
counter = last_doc['contactCounter']
time_counter = last_doc['counter']

# One-time initialization
toaster = ToastNotifier()

# Show notification whenever needed
toaster.show_toast("Notification!", "Alert!", threaded=True,
                   icon_path=None, duration=3)  # 3 seconds

# To check if any notifications are active,
# use `toaster.notification_active()`
import time
while toaster.notification_active():
    time.sleep(0.1)