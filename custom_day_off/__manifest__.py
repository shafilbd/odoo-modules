# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Employee Leave days',
    'description': """
        Employee can apply for their Paid leave to administrator.
    """,
    'author': "Promate Techonologies",
    'website': "https://www.promate.net",
    'version': '0.1',
    'sequence':-100,
    'category': 'Promate Tools',
    'depends': ['base', 'hr', 'hr_org_chart',],
    'data' : [
        'views/form_apply_for_leave.xml',
        'views/all_leave_list.xml',
        'views/all_leave_list_2.xml',
        'views/day_leave_data_update.xml'
    ],
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    'application': True,
    'assets' : {
        'web.assets_frontend': [
            'custom_day_off/static/src/css/dayoff-main.css',
            'custom_day_off/static/src/js/date-picker.js',
        ],
    },
    'license' : 'LGPL-3'
}

