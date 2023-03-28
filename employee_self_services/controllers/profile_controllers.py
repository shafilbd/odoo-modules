# -*- coding: utf-8 -*-

import base64

from odoo import http
from odoo.http import content_disposition, Controller, request, route
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.tools.mimetypes import guess_mimetype


class MyAccount(Controller):
    @http.route(['/my/home'],  type="http", auth="user", website=True)
    def portal_my_skip(self, **kw):
        # details = http.request.env['get.details']
        additional= http.request.env['hr.employee'].search([]) #('partner_id', '=', request.env.user.partner_id.id)
        response = request.render("employee_self_services.portal_layout_extra", {'addition': additional})
        response.headers['X-Frame-Options'] = 'DENY'
        return response

    @http.route(['/my/account'], type="http", auth="user", website=True)
    def portal_my_accounts(self, **kw):
        return 'hello'