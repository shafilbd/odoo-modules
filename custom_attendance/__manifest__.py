# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'External HR Attendance',
    'description': """
        External HR Attendance Portal to check in and out timing for employee.
    """,
    'author': "Promate Techonologies",
    'website': "https://www.promate.net",
    'version': '0.1',
    'sequence':-100,
    'category': 'Promate Attendance Tools',
    'depends': ['base','portal','hr', 'hr_org_chart',],
    'data' : [
        'views/check_in_attedance.xml',
        'views/all_attendance_list_template.xml',
        'views/delay_time_check_out.xml'
    ],
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    'application': True,
    'assets' : {
        'web.assets_frontend': [
            'custom_attendance/static/src/js/check_in.js',
            'custom_attendance/static/src/css/check_in.css',
        ],
    },
    'license' : 'LGPL-3'
}


