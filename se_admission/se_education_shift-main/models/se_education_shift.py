# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SeEducationShift(models.Model):
    _name = 'se.education.shift'
    _description = 'Education Shift'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', readonly=True)
    education_shift_code = fields.Char(string='Education Shift Code', track_visibility='onchange')
    # company_id = fields.Many2one(comodel_name='res.company', default=lambda self: self.env.user.company_id.id)
    note = fields.Text(string='Note')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('done', 'Confirmed'),
            ('cancel', 'Canceled'),
        ],
        string='State',
        default='draft',
        track_visibility='onchange',
        store=True
    )

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Code already exists!'),
        ('name_unique', 'unique(name)', 'Name already exists!'),
    ]

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('se.education.shift')
        res = super(SeEducationShift, self).create(vals)
        return res

    #will add this function after creating payment module

    # def unlink(self):
    #     for line in self:
    #         if line.state == 'done':
    #             raise UserError("You cannot delete an entry which has been validated.")
    #     res = super(SePaymentCategory, self).unlink()
    #     return res

    def action_validate(self):
        for line in self:
            line.state = 'done'

    def action_cancel(self):
        for line in self:
            line.state = 'draft'

