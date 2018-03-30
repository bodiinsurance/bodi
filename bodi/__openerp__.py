# -*- coding: utf-8 -*-
##############################################################################
#
#    Asterisk Technologies LLC, Enterprise Management Solution
#    Copyright (C) 2013-2015 Asterisk Technologies LLC (<http://www.erp.mn/, http://asterisk-tech.mn/&gt;). All Rights Reserved
#
#    Email : info@asterisk-tech.mn
#    Phone : 976 + 88005462, 976 + 94100149
#
##############################################################################

{
    "name": "Бодь - Дүрэм",
    "version": "1.0",
    "author": "Asterisk Technologies LLC",
    "description": """
        Бодь даатгал компаний дотоод дүрэм журмыг агуулна.
""",
    'website': "http://www.bodi-insurance.com",
    "category": "Mongolian Modules",
    "init": [],
    "data": [
        'views/bodi_view.xml',
    ],
    "active": False,
    "installable": True,
    'application': True,
    'icon': '/bodi/static/img/bodi_logo.jpeg',
    'qweb': ['static/src/xml/*.xml'],

    'contributors': ['Sugarsukh Sukhbaatar <sugarsukh@asterisk-tech.mn>'],
}
