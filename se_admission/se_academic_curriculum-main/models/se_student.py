# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class SeStudent(models.Model):
    _inherit = "se.student"
    _description = 'Students'

    student_type_id = fields.Many2one(comodel_name='se.student.type',
                                      string='Student Type',
                                      track_visibility='onchange')
    education_shift_id = fields.Many2one(comodel_name='se.education.shift',
                                         string='Education Shift',
                                         track_visibility='onchange')
    batch_id = fields.Many2one(comodel_name='se.batch',
                               string='Batch',
                               track_visibility='onchange')
    program_id = fields.Many2one(comodel_name="se.program",
                                string="Program",
                                store=True)
    # curriculum_id = fields.Many2one(comodel_name='se.academic.curriculum', string='Curriculum', domain=[('active','=',True)], track_visibility='onchange')
    # syllabus_id = fields.Many2one(comodel_name='se.academic.syllabus', string='Syllabus', domain=[('active','=',True)], track_visibility='onchange')
    # payment_scheme_id = fields.Many2one(comodel_name='op.academic.payment.scheme', string='Payment Scheme', domain=[('active','=',True)], track_visibility='onchange')
    # payment_scheme_currency_id = fields.Many2one(comodel_name='res.currency', string='Payment Scheme Currency', track_visibility='onchange')
    # student_syllabus_line_ids = fields.One2many(comodel_name='op.student.syllabus.line', inverse_name="student_id", string="Student Syllabus Lines", track_visibility='onchange')
    semester_id = fields.Many2one(comodel_name='se.semester',
                                  string='Semester',
                                  domain=[('is_active','=',True)],
                                  track_visibility='onchange')
    semester_year = fields.Date(string='Year',
                                track_visibility='onchange')
    semester_year_string = fields.Char(string='Year',
                                       track_visibility='onchange')
    semester_type = fields.Many2one(comodel_name='se.semester.type',
                                    string='Semester Type',
                                    related="semester_id.semester_type_id",
                                    store=True,
                                    track_visibility='onchange')

    
    @api.model
    def create(self, vals):
        res = super(SeStudent, self).create(vals)
        if 'syllabus_id' in vals.keys():
            self.get_student_syllabus_lines(res.id)
        return res
    

    def write(self, vals):
        res = super(SeStudent, self).write(vals)
        student = self.env['se.student'].browse(self.id)
        if 'syllabus_id' in vals.keys():
            self.get_student_syllabus_lines(student.id)
        return res
    

    # def get_student_syllabus_lines(self, student_id):
    #     student = self.env['se.student'].browse(student_id)
    #     student_syllabus_lines_all = self.env['op.student.syllabus.line'].search([('student_id','=',student.id)])
    #     for item in student_syllabus_lines_all:
    #         item.write({
    #             'is_listed_newbie': False
    #         })
    #
    #     student_syllabus_line_list = []
    #     for syllabus_line in student.syllabus_id.syllabus_line_ids:
    #         student_syllabus_lines = self.env['op.student.syllabus.line'].search([('student_id','=',student.id),('subject_id','=',syllabus_line.subject_id.id)])
    #         if student_syllabus_lines:
    #             for student_syllabus_line in student_syllabus_lines:
    #                 student_syllabus_line.write({
    #                     'is_listed_newbie': True
    #                 })
    #         else:
    #             amount = 0
    #             if student.student_type_id and student.education_shift_id and syllabus_line.subject_id:
    #                 amount = self.get_syllabus_subject_amount(syllabus_line.subject_id.id, syllabus_line.subject_id.grade_weightage)
    #
    #             student_syllabus_line_list.append({
    #                 'currency_id': student.payment_scheme_currency_id.id,
    #                 'amount': amount,
    #                 'program_id': student.syllabus_id.program_id.id,
    #                 'semester_type_id': student.syllabus_id.semester_type_id.id,
    #                 'level_id': syllabus_line.level_id.id,
    #                 'term_id': syllabus_line.term_id.id,
    #                 'syllabus_type_id': syllabus_line.syllabus_type_id.id,
    #                 'subject_id': syllabus_line.subject_id.id,
    #                 'subject_display_name': syllabus_line.subject_display_name,
    #                 'student_id': student.id
    #             })
    #
    #     student_syllabus_lines_deleted = self.env['op.student.syllabus.line'].search([('student_id','=',student.id),('is_listed_newbie','=',False)])
    #     for item in student_syllabus_lines_deleted:
    #         item.unlink()
    #
    #     if student_syllabus_line_list:
    #         self.env['op.student.syllabus.line'].create(student_syllabus_line_list)
    #

    # def get_syllabus_subject_amount(self, subject_id, grade_weightage):
    #     amount = 0
    #     if subject_id:
    #         subject = self.env['se.subject'].browse(subject_id)
    #         if self.payment_scheme_id and self.student_type_id and self.education_shift_id and subject:
    #             payment_scheme_line = self.env['op.academic.payment.scheme.line'].search([
    #                 ('payment_scheme_id','=',self.payment_scheme_id.id),
    #                 ('student_type_id','=',self.student_type_id.id),
    #                 ('education_shift_id','=',self.education_shift_id.id),
    #                 ('payment_category_id','=',subject.payment_category_id.id)
    #             ], limit=1)
    #             amount = payment_scheme_line.amount * grade_weightage
    #     return amount

