import base64
import json

from odoo import http
import requests
from odoo.http import content_disposition, Controller, request, route
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.tools.mimetypes import guess_mimetype
from werkzeug.utils import redirect
from datetime import datetime


class StoreAttendanceHour(Controller):
    @route(['/my/attendance'], type='http', auth='user', website=True)
    def Attendance(self, **kw):
        LoginUserId = request.session.uid
        dol = request.env['hr.employee'].sudo().search([('user_id', '=', LoginUserId)])
        # get the time delay value
        delay_time = dol.deplay_id
        print(delay_time)
        # print(employe_id.user_id.id)
        #print(dol.id)
        #print('image')
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        image_url_1920 = base_url + '/web/image?' + 'model=hr.employee&id=' + str(dol.id) + '&field=avatar_128'
        print(image_url_1920)
        restol = {'id': dol, 'profile': image_url_1920, 'delay_times': delay_time}
        response = request.render('custom_attendance.check_in_template', restol)
        return response

    @route(['/my/checkin'], type='http', auth='user', website=True, csrf=False)
    def CheckIn(self, **kw):
        # print(kw)
        sessionid = request.session.uid
        time = kw['time']
        print(time)
        emId = kw['employee_id']
        datetime_object = datetime.strptime(time, '%m/%d/%Y %H:%M:%S')
        print(type(datetime_object))
        Check_in = datetime.now()
        # print(Check_in)
        # i = Check_in.strftime('%Y-%m-%d %H:%M:%S')
        # print(i)

        dol = request.env['hr.attendance'].sudo().search([('employee_id', '=', emId)])
        kel = dol.create({'check_in': datetime_object})
        print(kel)

    @route(['/my/checkout'], type='http', auth='user', website=True, csrf=False)
    def CheckOut(self, **kw):
        time = kw['time']
        # print(time)
        emId = int(kw['employee_id'])
        datetime_object = datetime.strptime(time, '%m/%d/%Y %H:%M:%S')
        # print(type(datetime_object))-------++++++++++++++++
        last_id = request.env['hr.attendance'].search([('employee_id', '=', emId)],  limit=1, order='id desc')
        # print(Check_out)
        # print(last_id)
        kels = last_id.update({'check_out': datetime_object})
        print(kels)

    @route(['/my/all-attendance-list'], type='http', auth='user', website=True, csrf=False)
    def CheckAllAttendance(self, **kw):
        sessionid = request.session.uid
        co = request.env['hr.employee'].sudo().search([('user_id', '=', sessionid)])
        dol = request.env['hr.attendance'].sudo().search([('employee_id', '=', co.id)])
        # total_hour = {}
        # total_hour['name'] = []
        # total_hour['check_in'] = []
        # total_hour['check_out'] = []
        # total_hour['hours'] = []
        # for k in dol:
        #     print(type(k))
        #     # print(k.worked_hours)
        #     TotalHours = k.check_out - k.check_in
        #     i = str(TotalHours)
        #
        #     # mon, sec = divmod(k.worked_hours, 60)
        #     # hr, mon = divmod(k.worked_hours, 60)
        #     # print("%d:%02d:%02d" % (hr, mon, sec))
        #     total_hour['name'].append(k.employee_id.name)
        #     total_hour['check_in'].append(str(k.check_in))
        #     total_hour['check_out'].append(str(k.check_out))
        #     total_hour['hours'].append(i)
        # print(total_hour)
        # res = {'data': {'name': total_hour['name'], 'check_in': total_hour['check_in'], 'check_out': total_hour['check_out']}}
        # print(res)
        res ={'data': dol}
        # print(type(dol))
        response = request.render('custom_attendance.all_attendance_list_template', res)
        return response



