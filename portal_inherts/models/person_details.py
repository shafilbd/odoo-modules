import logging
from odoo import api, fields, models

_logger = logging.info('FYI: ')

class GetTheDetails(models.Model):
    _inherit = "hr.employee"

    @api.model
    def create(self, vals):
        # In the vals you will have the work email and all other details
        # compare the email with the mail of users
        user_rec = self.env['res.users'].search([('login', '=', vals['work_email'])], limit=1)
        vals['user_id'] = user_rec.id
        res = super(GetTheDetails, self).create(vals)
        return res

