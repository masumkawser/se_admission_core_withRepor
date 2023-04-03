# -*- coding: utf-8 -*-
# from odoo import http


# class SeCampusFacility(http.Controller):
#     @http.route('/se_campus_facility/se_campus_facility', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/se_campus_facility/se_campus_facility/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('se_campus_facility.listing', {
#             'root': '/se_campus_facility/se_campus_facility',
#             'objects': http.request.env['se_campus_facility.se_campus_facility'].search([]),
#         })

#     @http.route('/se_campus_facility/se_campus_facility/objects/<model("se_campus_facility.se_campus_facility"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('se_campus_facility.object', {
#             'object': obj
#         })
