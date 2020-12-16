# -*- coding: utf-8 -*-
# from odoo import http


# class Soportes(http.Controller):
#     @http.route('/soportes/soportes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/soportes/soportes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('soportes.listing', {
#             'root': '/soportes/soportes',
#             'objects': http.request.env['soportes.soportes'].search([]),
#         })

#     @http.route('/soportes/soportes/objects/<model("soportes.soportes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('soportes.object', {
#             'object': obj
#         })
