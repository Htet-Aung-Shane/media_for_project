{
    "name": "Media For Project",
    "description": "To add media at project ",
    "author": "MT Tech",
    'version': '17.0.0.0',
    "application": True,
    "installable": True,
    "license": "LGPL-3",
    "depends": ["project"],
    "data": [
        "security/ir.model.access.csv",
        "views/project_ext.xml",
    ],
    'assets': {
        'web.assets_backend': {
            'media_x_project/static/src/js/image_preview_widget.js',
            'media_x_project/static/src/xml/widget_image_preview.xml',
        }
    },
}
