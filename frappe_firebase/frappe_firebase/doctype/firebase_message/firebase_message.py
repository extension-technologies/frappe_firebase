# Copyright (c) 2022, Vinay Rawat and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe_firebase.config.basic import send_notification
from frappe_firebase.frappe_firebase.doctype.firebase_logs.firebase_logs import frappe_log

class FirebaseMessage(Document):
	def on_submit(self):
		firebase_settings = frappe.get_doc('Firebase Service Account Settings')
		if (firebase_settings.get('enable_push_notifications') == 0):
			frappe.throw('Push notifications are disabled')
			return frappe_log('Firebase Service Account Settings', 'Push notifications are disabled', 'send_notification')
		additional_data = {}
		for property in self.properties:
			additional_data[property.key] = property.value
		send_notification(
			title=self.title,
			body=self.message,
			topic=self.topic,
			additional_data=additional_data
		)
	def before_cancel(self):
		frappe.msgprint('Cancelling this message will not cancel the notification sent to the topic')
