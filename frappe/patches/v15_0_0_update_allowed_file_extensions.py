# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe


def execute():
	"""Add browser compatibility warning for TIFF and HEIC formats"""
	
	# Get current system settings
	system_settings = frappe.get_single("System Settings")
	
	# If allowed_file_extensions is not set, we don't need to do anything
	# Let users configure as needed
	
	# If it's set and includes TIFF or HEIC, add a comment about browser compatibility
	if system_settings.allowed_file_extensions:
		lines = system_settings.allowed_file_extensions.split('\n')
		has_tiff = any(line.strip().upper() in ['TIFF', 'TIF'] for line in lines)
		has_heic = any(line.strip().upper() == 'HEIC' for line in lines)
		
		if has_tiff or has_heic:
			print("Note: TIFF and HEIC formats are allowed but may not display properly in all browsers.")
			print("Consider adding a warning message for users uploading these formats.")
	
	print("System settings checked for TIFF/HEIC compatibility") 