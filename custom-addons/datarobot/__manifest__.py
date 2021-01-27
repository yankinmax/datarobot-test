{
    "name": "Datarobot Home Test",
    "version": "1",
    "category": "Website",
    "author": 'Maksym Yankin | @yankinmax',
    "description": """
        Used to guess column types on a publicly available Google Sheet,
    """,
    "depends": ['website', 'portal'],
    "data": [
        'views/website_form.xml',
        'views/website_data.xml',
        'views/portal_templates.xml',
    ],
    "installable": True,
    "auto_install": False,
}
