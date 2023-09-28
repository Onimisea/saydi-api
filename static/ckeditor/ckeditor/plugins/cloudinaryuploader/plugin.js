CKEDITOR.plugins.add("cloudinaryuploader", {
  icons: "cloudinaryuploader", // Icon for the button in the CKEditor toolbar.

  // This function is called when the plugin is loaded.
  init: function (editor) {
    // Add a button to CKEditor's toolbar that opens the Cloudinary image upload widget.
    editor.ui.addButton("CloudinaryUploader", {
      label: "Cloudinary Uploader",
      command: "openCloudinaryUploader",
      toolbar: "Custom",
      icon: CKEDITOR.getUrl(this.path + "cloudinaryuploader.png"), // Use CKEditor's URL helper to get the correct path.
    });

    // Define a CKEditor command to open the Cloudinary image upload widget.
    editor.addCommand("openCloudinaryUploader", {
      exec: function (editor) {
        var cloudinaryUploader = cloudinary.createUploadWidget(
          {
            cloudName: "deneyjtsc",
            uploadPreset: "ykhk5pgq",
          },
          function (error, result) {
            if (!error && result && result.event === "success") {
              // console.log(result.info.secure_url);

              // Insert the image URL into the CKEditor here.
              editor.insertHtml('<img src="' + result.info.secure_url + '">');
            }
          }
        );

        // Open the Cloudinary image upload widget here.
        cloudinaryUploader.open();
      },
    });
  },
});
