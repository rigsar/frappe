# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
from frappe.desk.doctype.global_search_settings.global_search_settings import update_global_search_doctypes

def install():
	update_genders()
	update_salutations()
	update_global_search_doctypes()
	setup_email_linking()

@frappe.whitelist()
def update_genders():
	default_genders = [_("Male"), _("Female"), _("Other"),_("Transgender"), _("Genderqueer"), _("Non-Conforming"),_("Prefer not to say")]
	records = [{'doctype': 'Gender', 'gender': d} for d in default_genders]
	for record in records:
		frappe.get_doc(record).insert(ignore_permissions=True, ignore_if_duplicate=True)

@frappe.whitelist()
def update_salutations():
	default_salutations = [_("Mr"), _("Ms"), _('Mx'), _("Dr"), _("Mrs"), _("Madam"), _("Miss"), _("Master"), _("Prof")]
	records = [{'doctype': 'Salutation', 'salutation': d} for d in default_salutations]
	for record in records:
		doc = frappe.new_doc(record.get("doctype"))
		doc.update(record)
		doc.insert(ignore_permissions=True, ignore_if_duplicate=True)

def setup_email_linking():
	doc = frappe.get_doc({
		"doctype": "Email Account",
		"email_id": "email_linking@example.com",
	})
	doc.insert(ignore_permissions=True, ignore_if_duplicate=True)
