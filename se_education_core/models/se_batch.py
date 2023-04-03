from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SeBatch(models.Model):
    _name = "se.batch"
    _inherit = "mail.thread"
    _description = "SmartEdu Batch"

    code = fields.Char('Code', required=True)
    start_date = fields.Date('Start Date', required=True, default=fields.Date.today())
    end_date = fields.Date('End Date', required=True)
    course_id = fields.Many2one(comodel_name='se.course',
                                string='Course',
                                required=True)
    active = fields.Boolean(default=True)
    name = fields.Char(string='Batch Name')
    code = fields.Char(string='Code')
    batch_no = fields.Char(string='Batch No')
    start_date = fields.Date(string='Start Date', default=fields.Date.context_today)
    end_date = fields.Date(string='End Date', default=fields.Date.context_today)
    program = fields.Char(string='Program')
    semester_id = fields.Many2one(comodel_name='se.semester',
                                  string='Semester ',)
    semester_type_id = fields.Many2one(comodel_name='se.semester.type',
                                       string='Semester Type ',
    )
    year = fields.Date(string='Year', default=fields.Date.context_today)
    curriculum = fields.Char(string='Curriculum')
    syllabus = fields.Char(string='Syllabus')
    payment_scheme = fields.Char(string='Payment Scheme')
    active = fields.Boolean(string='Active', default=True)
    note = fields.Text(string='Note')

    _sql_constraints = [
        ('unique_batch_code',
         'unique(code)', 'Code should be unique per batch!')]

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for record in self:
            start_date = fields.Date.from_string(record.start_date)
            end_date = fields.Date.from_string(record.end_date)
            if start_date > end_date:
                raise ValidationError(
                    _("End Date cannot be set before Start Date."))

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self.env.context.get('get_parent_batch', False):
            lst = []
            lst.append(self.env.context.get('course_id'))
            courses = self.env['se.course'].browse(lst)
            while courses.parent_id:
                lst.append(courses.parent_id.id)
                courses = courses.parent_id
            batches = self.env['se.batch'].search([('course_id', 'in', lst)])
            return batches.name_get()
        return super(SeBatch, self).name_search(
            name, args, operator=operator, limit=limit)

    # @api.model
    # def get_import_templates(self):
    #     return [{
    #         'label': _('Import Template for Batch'),
    #         'template': '/openeducat_core/static/xls/op_batch.xls'
    #     }]
