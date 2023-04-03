from odoo import models, fields, api


class SeDepartment(models.Model):
    _name = "se.department"
    _description = "SmartEdu Department"

    name = fields.Char('Name')
    code = fields.Char('Code')
    parent_id = fields.Many2one('se.department', 'Parent Department')

    @api.model
    def create(self, vals):
        department = super(SeDepartment, self).create(vals)
        self.env.user.write({'department_ids': [(4, department.id)]})
        return department
