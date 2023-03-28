# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Employee Self Service',
    'description': """
        Employee Self Management system to get the data of the employees.
    """,
    'author': "Promate Techonologies",
    'website': "https://www.promate.net",
    'version': '0.1',
    'sequence':-100,
    'category': 'Promate Tools',
    'depends': ['base', 'hr', 'hr_org_chart'],
    'data' : [
        'views/show_employee_age_view.xml',
    ],
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    'license' : 'LGPL-3'
}

