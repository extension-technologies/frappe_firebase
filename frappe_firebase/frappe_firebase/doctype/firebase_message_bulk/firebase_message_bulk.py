# Copyright (c) 2022, Vinay Rawat and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe_firebase.config.basic import send_all_notification

class FirebaseMessageBulk(Document):
	def on_submit(self):
		send_all_notification(self)
