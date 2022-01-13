import firebase_admin
from firebase_admin import messaging
from firebase_admin.credentials import Certificate
from frappe_firebase.config.firebase_settings import getCred
import frappe
from frappe_firebase.frappe_firebase.doctype.firebase_logs.firebase_logs import frappe_log

def init_app(app):
    if (len(firebase_admin._apps) == 0):
        firebase_admin.initialize_app(Certificate(getCred()))
    

def send_notification(data, topic):
    doc = frappe.get_doc('Firebase Service Account Settings')
    if(doc.get('enable_push_notifications') == 0):
        return frappe_log('Firebase Service Account Settings', 'Push notifications are disabled', 'send_notification')
    init_app()
    message = messaging.Message(
        topic=topic,
        notification=messaging.Notification(
            body=data.get("body"),
            title=data.get("title")
        )
    )
    response = messaging.send(message)
    frappe_log('Firebase Message', 'Message sent', response)

def send():
    send_notification({'title': 'Basic notification for customers', 'body': 'Body of my notification'}, 'customer')