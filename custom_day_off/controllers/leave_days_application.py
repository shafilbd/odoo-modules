import base64
import json

from odoo import http
import requests
from odoo.http import content_disposition, Controller, request, route
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.tools.mimetypes import guess_mimetype
from werkzeug.utils import redirect
from datetime import datetime

File_Type = ['application/pdf', 'image/jpeg', 'image/png']  # allowed file type

class ApplicationForLeave(Controller):
    @route(['/my/dayoff-application'], type='http', auth='user', website=True)
    def dayoffapplication(self, **kw):
        leavetypes = request.env['hr.leave.type'].sudo().search([])
        sessionid = request.session.uid
        co = request.env['hr.employee'].sudo().search([('user_id', '=', sessionid)])
        print(co.name)
        res = {'leavetype': leavetypes, 'user': co}
        response = request.render('custom_day_off.form_to_apply_leave', res)
        return response

    @route(['/my/apply-for-dayoff'], type="http", auth="user", website=True, csrf=False)
    def DayOffApplicationSubmit(self, **kw):
        sessionid = request.session.uid
        dayOffTypes = int(kw['DayoffTypes'])
        EmpId = int(kw['EmployeeId'])
        DayStart = kw['DayStart']
        DayEnd = kw['DateEnd']
        des = kw['Descrip']
        # addfile = kw['AddiFiles']

        DateStartConvert = datetime.strptime(DayStart, '%m/%d/%Y')
        DateEndConvert = datetime.strptime(DayEnd, '%m/%d/%Y')
        print(DateStartConvert)
        print(DateEndConvert)
        # print(addfile)
        # GetTheAttch = request.env['ir.attachment'].sudo().search([])
        # if addfile:
        #     attachment = addfile.read()
        #     mimetype = guess_mimetype(base64.b64decode(base64.encodebytes(attachment)))
        #     if mimetype in File_Type:
        #         GetTheAttch.write({'datas': base64.encodebytes(attachment)})
        # LastAttachedId = self.env['ir.attachment'].search(['create_uid', '=', sessionid])[-1].id
        # 'attachment_ids': LastAttachedId,

        emple = request.env['hr.leave'].sudo().search([('user_id', '=', sessionid)])
        AddDays = emple.create({'holiday_status_id' : dayOffTypes,
                                'employee_id': EmpId,
                                'date_from': DateStartConvert,
                                'date_to': DateEndConvert,
                                'name': des})
        print(AddDays)

    @route(['/my/all-leave-list'], type="http", auth="user", website=True)
    def AllLeaveLists(self):
        sessionid = request.session.uid
        emple = request.env['hr.leave'].sudo().search([('user_id', '=', sessionid)])
        attached = emple.supported_attachment_ids.id
        getAttached = request.env['ir.attachment'].sudo().search([('id', '=', attached)])
        print(attached)
        img_url = "/web/image/ir.attachment/%s/datas" % getAttached.id
        print(img_url)
        datas = {'details': emple, 'attah': getAttached}
        print(emple.supported_attachment_ids.id)
        res = request.render('custom_day_off.all_day_leave_list_template', datas)
        return res


    @route(['/my/dayoff-application-2'], type='http', auth='user', website=True)
    def dayoffapplications(self, **kw):
        leavetypes = request.env['hr.leave.type'].sudo().search([])
        sessionid = request.session.uid
        co = request.env['hr.employee'].sudo().search([('user_id', '=', sessionid)])
        print(co.name)
        res = {'leavetype': leavetypes, 'user': co}
        response = request.render('custom_day_off.form_to_apply_leave_2', res)
        return response


    @route(['/my/all-leave-lists-2'], type="http", auth="user", website=True)
    def AllLeaveList2(self, **kw):
        sessionid = request.session.uid
        dayOffTypes = int(kw['DayoffTypes'])
        EmpId = int(kw['EmployeeId'])
        DayStart = kw['DayStart']
        DayEnd = kw['DateEnd']
        totalDays = float(kw['totaldays'])
        # file = kw.get('attachment')
        des = kw['Descrip']
        GetTheAttch = request.env['ir.attachment']
        if kw.get('attachment', False):
            name = kw.get('attachment').filename
            attachment = kw.get('attachment').read()
                # mimetype = guess_mimetype(base64.b64decode(base64.encodebytes(attachment)))
                # if mimetype in File_Type:
            attachment_id = GetTheAttch.create({
                'name': name,
                'type': 'binary',
                'datas': base64.b64encode(attachment),
                'res_model': "hr.leave",
                'res_id': sessionid,
            })
        else:
            attachment_id = 0
        # LastAttachedId = request.env['ir.attachment'].search(['create_uid', '=', sessionid])[-1].id
        DateStartConvert = datetime.strptime(DayStart, '%m/%d/%Y')
        DateEndConvert = datetime.strptime(DayEnd, '%m/%d/%Y')
        # print(attachment_id.id)
        #'supported_attachment_ids': LastAttachedId,
        emple = request.env['hr.leave'].sudo().search([('user_id', '=', sessionid)])
        AddDays = emple.create({'holiday_status_id': dayOffTypes,
                                'employee_id': EmpId,
                                'date_from': DateStartConvert,
                                'date_to': DateEndConvert,
                                'supported_attachment_ids': attachment_id,
                                'number_of_days': totalDays,
                                'name': des})

        # print(AddDays)
        res = request.redirect('/my/all-leave-list')
        return res

    @route(['/my/edit/day-leave'], type="http", auth="user", website=True)
    def UpdateLeaveData(self, **kw):
        leaveid = kw.get('leaveid')
        em = request.env['hr.leave'].sudo().search([('id', '=', leaveid)])
        print(em.state)
        ks = {'details': em}
        res = request.render('custom_day_off.day_leave_data_update_template', ks)
        return res

    @route(['/my/edit/day-leave-update'], type="http", auth="user", website=True)
    def UpdateDatasLeave(self, **kw):
        sessionid = request.session.uid
        leaveid = kw['leaveid']
        dayOffTypes = int(kw['DayoffTypes'])
        EmpId = int(kw['EmployeeId'])
        DayStart = kw['DayStart']
        DayEnd = kw['DateEnd']
        des = kw['Descrip']
        GetTheAttch = request.env['ir.attachment']
        if kw.get('attachment', False):
            name = kw.get('attachment').filename
            attachment = kw.get('attachment').read()
                # mimetype = guess_mimetype(base64.b64decode(base64.encodebytes(attachment)))
                # if mimetype in File_Type:
            attachment_id = GetTheAttch.create({
                'name': name,
                'type': 'binary',
                'datas': base64.b64encode(attachment),
                'res_model': "hr.leave",
                'res_id': sessionid,
            })
        else:
            attachment_id = 0


        DateStartConvert = datetime.strptime(DayStart, '%m/%d/%Y')
        DateEndConvert = datetime.strptime(DayEnd, '%m/%d/%Y')
        emple = request.env['hr.leave'].sudo().search([('user_id', '=', leaveid)])
        updateDate = emple.create({'holiday_status_id': dayOffTypes,
                                'employee_id': EmpId,
                                'date_from': DateStartConvert,
                                'date_to': DateEndConvert,
                                'supported_attachment_ids': attachment_id,
                                'name': des})
        print(updateDate)


    @route(['/my/deleteattach'], type="http", auth="user", website=True)
    def UpdateAttachmentFiles(self, **kw):
        attchmentId = kw['id']
        GetTheAttch = request.env['ir.attachment'].sudo().search([('id', '=', attchmentId)]).unlink()
        # res = request.redirect('/my/edit/day-leave?leaveid=29').format()
        # return res