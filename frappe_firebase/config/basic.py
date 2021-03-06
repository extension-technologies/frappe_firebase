from email import message
import firebase_admin
from firebase_admin import messaging
from firebase_admin.credentials import Certificate
from frappe_firebase.config.firebase_settings import getCred
import frappe
from frappe_firebase.frappe_firebase.doctype.firebase_logs.firebase_logs import frappe_log

def init_app():
    if (len(firebase_admin._apps) == 0):
        firebase_admin.initialize_app(Certificate(getCred()))
    

def send_notification(title, body, topic=None, additional_data=None, fcm_token=None):
    doc = frappe.get_doc('Firebase Service Account Settings')
    if(doc.get('enable_push_notifications') == 0):
        return frappe_log('Firebase Service Account Settings', 'Push notifications are disabled', 'send_notification')
    init_app()
    message = messaging.Message(
        topic=topic,
        token=fcm_token,
        notification=messaging.Notification(
            body=body,
            title=title
        ),
        data=additional_data
    )
    try:
        response = messaging.send(message)
    except Exception as e:
        frappe_log('Unable to send notification', message, e)
    # frappe_log('Firebase Message', 'Message sent', response)

def send():
    send_notification({'title': 'Basic notification for customers', 'body': 'Body of my notification'}, 'customer')