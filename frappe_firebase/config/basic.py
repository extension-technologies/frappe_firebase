import firebase_admin
from firebase_admin import messaging
from firebase_admin.credentials import Certificate
from frappe_firebase.config.firebase_settings import getCred

default_app = firebase_admin.initialize_app(Certificate(getCred()))

def send_notification(data, topic):
    message = messaging.Message(
        topic=topic,
        notification={
            'title': data.get('title'),
            'body': data.get('body'),
            'sound': 'default',
            'click_action': data.get('click_action')
        }
    )
    response = messaging.send(message)
    return response

send_notification({'title': 'Basic notification for customers', 'body': 'Body of my notification'}, 'customer')