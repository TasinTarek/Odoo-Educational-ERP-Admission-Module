# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class SeAdmission(http.Controller):
     @http.route('/se_admission/se_application', website=True, auth='public')
     def index(self, **kw):
         return request.render("se_admission.admission_portal_form",{})

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
