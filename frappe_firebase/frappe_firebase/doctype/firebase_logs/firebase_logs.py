# Copyright (c) 2022, Vinay Rawat and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FirebaseLogs(Document):
	pass

@frappe.whitelist()
def frappe_log(title, message=None, reference=None):
	doc = frappe.new_doc('Firebase Logs')
	doc.log_title = title
	doc.log_message = message
	doc.reference = reference
	doc.insert()