# -*- coding: utf-8 -*-
{
    'name': 'Limit list rows number',
    'version': '1.1',
    'category': 'Usability',
    'summary': 'Let assign default value to limit number of rows in list views through xml',
    'description': '''
 The app is a tool to limit number of lines in lists (one2many, many2many) by default:
 * Standard Odoo opens 80 rows, but using the tree attribute <i>'limit_list'</i> you may assign any number
 * It simplifies form views, since you do not have to scroll a lot
 * You may switch to the next page by usual Odoo 'arrow' buttons
 * Observe the example in the 'Documentation' section to use it in your own modules.
    ''',
    'auto_install': False,
    'author': 'IT Libertas',
    'website': 'https://itlibertas.com',
    'depends': [

    ],
    'data': [
        'data/data.xml',
        'views/template.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [

    ],
    'js': [

    ],
    'demo': [

    ],
    'test': [

    ],
    'license': 'AGPL-3',
    'images': [
        'static/description/main.png',
    ],
    'update_xml': [

    ],
    'application': False,
    'installable': True,
    'private_category': False,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'post_load': 'post_load',
    'uninstall_hook': 'uninstall_hook',
    'external_dependencies': {
    },

}
