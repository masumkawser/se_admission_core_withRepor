from odoo import models, fields, api, _


class SeSubject(models.Model):
    _name = "se.subject"
    _inherit = "mail.thread"
    _description = "Subject"

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    grade_weightage = fields.Float('Grade Weightage')
    type = fields.Selection([
        ('theory', 'Theory'),
        ('practical', 'Practical'),
        ('both', 'Both'),
        ('other', 'Other')
    ], 'Type', default="theory", required=True)
    subject_type = fields.Selection([
        ('compulsory', 'Compulsory'),
        ('elective', 'Elective')
    ], 'Subject Type', default="compulsory", required=True)
    department_id = fields.Many2one(
        comodel_name='se.department',
        inverse_name='Department')
        # default=lambda self:
        # self.env.user.dept_id and self.env.user.dept_id.id or False)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_subject_code',
         'unique(code)', 'Code should be unique per subject!'),
    ]

    # @api.model
    # def get_import_templates(self):
    #     return [{
    #         'label': _('Import Template for Subjects'),
    #         'template': '/openeducat_core/static/xls/op_subject.xls'
    #     }]