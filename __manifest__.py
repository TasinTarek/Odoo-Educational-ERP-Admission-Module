# -*- coding: utf-8 -*-
{
    'name': "SmartEdu Admission",

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
    'depends': ['base',
                'se_campus_facility'],

    # always loaded
    'data': [
    # Security
        'security/ir.model.access.csv',
    #Views 
        'views/se_admission_views.xml',
        'views/se_application_views.xml',
    #Menus 
        'views/se_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
