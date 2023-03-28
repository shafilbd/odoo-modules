from odoo import api, fields, models


class CheckOutDelay(models.Model):
    _inherit = 'hr.employee'

    deplay_id = fields.Integer('Manage Deplay Minutes', default=5)



