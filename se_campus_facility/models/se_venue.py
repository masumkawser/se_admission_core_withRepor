# -*- coding: utf-8 -*-

from odoo import models, fields, api


class se_campus_facility(models.Model):
     _name = 'se.venue'
     _description = 'se campus facility'
     
     name = fields.Text(string='Name')
     note = fields.Text(string="Note")
     is_admission_venue = fields.Boolean(string="Admission Venue", default=False)
     is_default_venue = fields.Boolean(string="Default Venue", default=False)
     facility_type_id = fields.Char(string = "Venue Type")
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
