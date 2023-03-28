from odoo import api, fields, models

class AgeInherit(models.Model):
    _inherit = "hr.employee"

    age_uid = fields.Integer('Employee Age')
    employee_type_uid = fields.Selection([
        ('full-time', 'Full Time'),
        ('parttime', 'Part Time'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", tracking=True,default='full-time', string='Employee Type')
    multi_address_id = fields.Many2one('hr.employee', 'Employee Working Address', groups="hr.group_hr_user",tracking=True, help='Employee Working Address')
    multi_addresses_id = fields.Many2one('hr.multiaddress', 'Employee Working Address')

