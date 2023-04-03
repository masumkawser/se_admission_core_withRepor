from odoo import api, fields, models


class SeCourse(models.Model):
    _name = 'se.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'SmartEdu Course'

    name = fields.Char('Name')
    note = fields.Char('Note')
    code = fields.Char('Code')
    active = fields.Boolean('Active')
    parent_id = fields.Many2one('se.course', 'Parent Course')
    evaluation_type = fields.Selection(
        [('normal', 'Normal'), ('GPA', 'GPA'),
         ('CWA', 'CWA'), ('CCE', 'CCE')],
        'Evaluation Type', default="normal", required=True)
    subject_ids = fields.Many2many('se.subject', string='Subject(s)')
    max_unit_load = fields.Float("Maximum Unit Load")
    min_unit_load = fields.Float("Minimum Unit Load")
    department_id = fields.Many2one(comodel_name='se.department',
                                    string='Department')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_course_code',
         'unique(code)', 'Code should be unique per course!')]

    # @api.model
    # def get_import_templates(self):
    #     return [{
    #         'label': ('Import Template for Courses'),
    #         'template': '/openeducat_core/static/xls/op_course.xls'
    #     }]
