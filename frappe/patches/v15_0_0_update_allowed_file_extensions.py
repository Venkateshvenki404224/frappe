# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe


def execute():
	"""Update system settings to exclude unsupported image formats like TIFF and HEIC"""
	
	# Get current system settings
	system_settings = frappe.get_single("System Settings")
	
	# If allowed_file_extensions is not set, set it to our safe defaults
	if not system_settings.allowed_file_extensions:
		system_settings.allowed_file_extensions = """JPG
JPEG
PNG
GIF
WEBP
SVG
PDF
DOC
DOCX
XLS
XLSX
TXT
CSV
MP4
MOV"""
		system_settings.save()
		frappe.db.commit()
		print("Updated System Settings with safe file extensions (excluding TIFF/HEIC)")
	
	# If it's set but includes TIFF or HEIC, update it
	elif any(ext in system_settings.allowed_file_extensions.upper() for ext in ['TIFF', 'TIF', 'HEIC']):
		# Remove TIFF and HEIC from the list
		lines = system_settings.allowed_file_extensions.split('\n')
		filtered_lines = [line for line in lines if line.strip().upper() not in ['TIFF', 'TIF', 'HEIC']]
		
		# Add safe defaults if not present
		safe_defaults = ['JPG', 'JPEG', 'PNG', 'GIF', 'WEBP', 'SVG']
		for default in safe_defaults:
			if default not in filtered_lines:
				filtered_lines.append(default)
		
		system_settings.allowed_file_extensions = '\n'.join(filtered_lines)
		system_settings.save()
		frappe.db.commit()
		print("Removed TIFF/HEIC from System Settings allowed file extensions") 