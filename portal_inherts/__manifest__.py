# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'External Portal',
    'description': """
        External Portal to edit and update the portal in custom portal section.
    """,
    'author': "Promate Techonologies",
    'website': "https://www.promate.net",
    'version': '0.1',
    'sequence':-100,
    'category': 'Promate Tools',
    'depends': ['base','portal','hr', 'hr_org_chart'],
    'data' : [
        'views/template.xml',
        'views/account.xml',
        'views/employeelist.xml',
        'views/employee_update.xml'
    ],
    'demo' : [],
    'installable' : True,
    'auto_install' : False,
    'license' : 'LGPL-3'
}

