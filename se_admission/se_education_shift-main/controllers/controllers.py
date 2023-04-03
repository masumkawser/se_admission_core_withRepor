# -*- coding: utf-8 -*-
# from odoo import http


# class SeEducationShift(http.Controller):
#     @http.route('/se_education_shift/se_education_shift', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/se_education_shift/se_education_shift/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('se_education_shift.listing', {
#             'root': '/se_education_shift/se_education_shift',
#             'objects': http.request.env['se_education_shift.se_education_shift'].search([]),
#         })

#     @http.route('/se_education_shift/se_education_shift/objects/<model("se_education_shift.se_education_shift"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('se_education_shift.object', {
#             'object': obj
#         })
