# -*- coding: utf-8 -*-

import base64

from odoo import http
from odoo.http import content_disposition, Controller, request, route
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.tools.mimetypes import guess_mimetype


class MyAccount(Controller):
    @http.route(['/my/home'],  type="http", auth="user", website=True)
    def my_home(self, **kw):
        # details = http.request.env['get.details']
        # additional = http.request.env['get.details'].search(['user_id', '=', self.env.user.id], limit=1)  # ('partner_id', '=', request.env.user.partner_id.id)
        # additional = http.request.env['hr.employee'].search([])
        # res = {'addition': additional}
        partner = request.env.user.partner_id
        res = {'partners': partner}
        print(partner)
        print('Hello budy!')
        response = request.render("portal_inherts.portal_layout_extra", res)
        return response

    @http.route(['/get'], type="http", auth="public", website=True)
    def GetId(self):
        # partner = request.env.user.partner_id
        partner =request.env['res.users'].search([])
        sessionid = request.session.uid
        # print(partner)
        print(sessionid)
        # print('hello'+partner)
        # employe = http.request.env['get.details'].search(['users_id','=', self.env.user.id], limit=1)
        # res = {'addition': employe}
        # response = request.render("portal_inherts.portal_layout_extra", res)
        # return response
        # return 'Hello'

