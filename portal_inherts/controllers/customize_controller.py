# -*- coding: utf-8 -*-

import base64
import json

from odoo import http
import requests
from odoo.http import content_disposition, Controller, request, route
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.tools.mimetypes import guess_mimetype
from werkzeug.utils import redirect


class CusContoller(CustomerPortal):
    @route(['/my/accounts'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        values.update({
            'error': {},
            'error_message': [],
        })

        if post and request.httprequest.method == 'POST':
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            values.update(post)
            if not error:
                values = {key: post[key] for key in self.MANDATORY_BILLING_FIELDS}
                values.update({key: post[key] for key in self.OPTIONAL_BILLING_FIELDS if key in post})
                for field in set(['country_id', 'state_id']) & set(values.keys()):
                    try:
                        values[field] = int(values[field])
                    except:
                        values[field] = False
                values.update({'zip': values.pop('zipcode', '')})
                partner.sudo().write(values)
                if redirect:
                    return request.redirect(redirect)
                return request.redirect('/my/home')

        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])

        values.update({
            'partner': partner,
            'countries': countries,
            'states': states,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'redirect': redirect,
            'page_name': 'my_details',
        })
        response = request.render("portal_inherts.portal_my_details", values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response

    @http.route('/my/employee', type='http', auth="user", website=True)
    def portal_employee(self, **kw):
        # print(add)
        # print(id)
        data_cal = {}
        data_list = []
        additional = http.request.env['hr.employee'].search([])
        # additional = http.request.env['hr.employee'].search(['id', '=', self.id])
        # val =  http.request.env['hr.employee'].search(['age_uid'])
        # vals['user_id'] = additional.id
        # print(self.user_id)
        # myid =http.request.env.context.get('uid')
        useremail = ""
        username = request.env.user.partner_id

        for l in username:
            #print(l.email)
            useremail+=str(l.email)
        # know = self.env['res.users'].search([])
        # print(username)
        # print(myid)
        sessionid = request.session.uid

        for k in additional:
            # print(k.activity_user_id)
            # print(k.id)
            if k.user_id.id == sessionid:
                # print(k.data_cal)
                p = str(k.age_uid)
                name = str(k.name)
                email = str(k.work_email)
                data_list.append(name)
                data_list.append(email)
                data_list.append(p)
                data_cal['Name'] = k.name
                data_cal['Work_email'] = k.work_email
                data_cal['Age'] = k.age_uid
                print(additional.user_id)
        print(data_list)
            # print(k.user_id.id)
            # for i in k.user_id:
            #     print(i.id)
            #     if i == sessionid:
                # user = str(k.id) + str(k.work_email)
                    # print(i)
                    # print(k.user_partner_id)
                    #pass

        # res = {'addition': additional}
        # print(type(additional))\
        datas = {
            'values': data_list
        }
        # p = requests.get(additional).json()
        # print(p)
        # sort_total = sorted(list(data_cal.items()), key=lambda r: r[1], reverse=True)
        return request.render("portal_inherts.employee_lists", datas)

    # @http.route('/my/employee/<int:id>', type='http', auth="user", website=True)
    # def portal_employee_id(self, id, **kw):
    #     return 'hello'+id


class ListingAdded(Controller):
    @route(['/my/eup'], type='http', auth='user', website=True)
    def EmployeeList(self, redirect=None, **post):
        sessionid = request.session.uid
        dol = request.env['hr.employee'].sudo().search([('user_id', '=', sessionid)])
        print(dol.department_id.id)
        dols = request.env['hr.department'].sudo().search([])
        #print(dols.id)
        res = {'add': dol, 'dop': dols}
        response = request.render("portal_inherts.Portal_Data_Update", res)
        return response

    @route(['/my/update'], type='http', auth='user', website=True)
    def EmployeeDataUpdate(self, **kw):
        Dept_id = int(kw['depart'])
        Name = kw['name']
        email = kw['email']
        Age = kw['age']
        print(type(Dept_id))
        # additional = http.request.env['hr.employee'].search([])
        sessionid = request.session.uid
        # print(additional)
        # countries = request.env['hr.emplo-yee'].sudo().search([('user_id', '=', sessionid), ('', '<=', Age)])
        # print(countries)
        # department added the fields
        co = request.env['hr.employee'].sudo().search([('user_id', '=', sessionid)])
        col = co.update({'name': Name, 'work_email': email, 'age_uid': Age, 'department_id': Dept_id})
        users1 = http.request.env['res.users'].search([('id', '=', sessionid)])
        up = users1.update({'name': Name, 'email': email})
        print(up)
        # print(co)
        response = redirect('http://localhost:8069/my/home')
        return response
        # response = request.render("portal_inherts.Portal_Data_Update")
        # return response










