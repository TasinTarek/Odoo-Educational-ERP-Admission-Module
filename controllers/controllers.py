# -*- coding: utf-8 -*-
# from odoo import http


# class SeAdmission(http.Controller):
#     @http.route('/se_admission/se_admission', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/se_admission/se_admission/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('se_admission.listing', {
#             'root': '/se_admission/se_admission',
#             'objects': http.request.env['se_admission.se_admission'].search([]),
#         })

#     @http.route('/se_admission/se_admission/objects/<model("se_admission.se_admission"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('se_admission.object', {
#             'object': obj
#         })
