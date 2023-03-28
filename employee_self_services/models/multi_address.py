from odoo import api, fields, models

class MultiAddress(models.Model):
    _name = "hr.multiaddress"
    _description = "Employee Address"

    name = fields.Char('Employee working', readonly=False, related_sudo=False)