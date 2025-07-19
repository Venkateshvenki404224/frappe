frappe.ui.form.ControlAttachImage = class ControlAttachImage extends frappe.ui.form.ControlAttach {
	make_input() {
		super.make_input();

		let $file_link = this.$value.find(".attached-file-link");
		$file_link.popover({
			trigger: "hover",
			placement: "top",
			content: () => {
				return `<div>
					<img src="${this.get_value()}"
						width="150px"
						style="object-fit: contain;"
					/>
				</div>`;
			},
			html: true,
		});
	}
	set_upload_options() {
		super.set_upload_options();
		this.upload_options.restrictions.allowed_file_types = ["image/*"];
		// Add warning for unsupported formats
		this.upload_options.on_success = (file_doc) => {
			if (file_doc.file_name && (file_doc.file_name.toLowerCase().endsWith('.tiff') || 
				file_doc.file_name.toLowerCase().endsWith('.tif') || 
				file_doc.file_name.toLowerCase().endsWith('.heic'))) {
				frappe.show_alert({
					message: __('Warning: {0} format may not display properly in all browsers. Consider using JPG, PNG, or WebP for better compatibility.', [file_doc.file_name.split('.').pop().toUpperCase()]),
					indicator: "orange",
				});
			}
		};
	}
};
