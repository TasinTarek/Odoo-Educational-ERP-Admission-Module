# -*- coding: utf-8 -*-
{
    'name': "Smart Edu Admission",

    'summary': """
        Best Educational ERP in Smart Way.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Tasin Tarek",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/se_admission_views.xml',
        'views/se_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
