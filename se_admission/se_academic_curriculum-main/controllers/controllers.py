# -*- coding: utf-8 -*-
# from odoo import http


# class SeAcademicCurrilculum(http.Controller):
#     @http.route('/se_academic_curriculum/se_academic_curriculum', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/se_academic_curriculum/se_academic_curriculum/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('se_academic_curriculum.listing', {
#             'root': '/se_academic_curriculum/se_academic_curriculum',
#             'objects': http.request.env['se_academic_curriculum.se_academic_curriculum'].search([]),
#         })

#     @http.route('/se_academic_curriculum/se_academic_curriculum/objects/<model("se_academic_curriculum.se_academic_curriculum"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('se_academic_curriculum.object', {
#             'object': obj
#         })
