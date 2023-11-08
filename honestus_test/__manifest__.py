# Copyright 2023 Uladzislau Kakouka
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Honestus Test',
    'version': '16.0.1.0.0',
    'category': 'Other',
    'author': 'Uladzislau Kakouka',
    'website': 'https://example.tech',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'auth_signup',
        'product',
        'sale_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/auth_signup_login_templates.xml',
        'views/portal_templates.xml',
        'views/product_product_views.xml',
        'report/purchase_report_views.xml',
        'report/honestus_sql_task_report_views.xml.xml',
    ],
    'installable': True,
    'application': True,
}
