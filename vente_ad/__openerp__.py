# -*- coding: utf-8 -*-
{
    'name': "vente_ad",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report_sale_order_modify.xml',
        'sale_report.xml',
        'print_modify.xml',
        'sale_order_form_modify.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}