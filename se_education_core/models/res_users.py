from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'
    _description = 'User'

    name = fields.Char()
    department_ids = fields.Many2one(comodel_name='se.department',
                                     string='Allowed Department')