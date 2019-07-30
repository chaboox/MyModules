# -*- coding: utf-8 -*-
from openerp import fields, tools, api, models
from openerp.exceptions import ValidationError
from openerp.tools import amount_to_text_en
from openerp.tools.amount_to_text_en import amount_to_text
from openerp.tools.amount_to_text import amount_to_text_fr


class SaleOrderInherited(models.Model):
    _inherit='sale.order'
    #price_text = fields.Char(compute='textPrice', store='True')
    total_text = fields.Char(compute='textPrice', store='True')

    @api.depends('amount_total')
    def textPrice(self):
        for record in self:
            #record.total_text = str( record.amount_total )
            record.total_text =amount_to_text_fr(record.amount_total, 'dinars')

   
#     @http.route('/vente_ad/vente_ad/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vente_ad/vente_ad/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vente_ad.listing', {
#             'root': '/vente_ad/vente_ad',
#             'objects': http.request.env['vente_ad.vente_ad'].search([]),
#         })

#     @http.route('/vente_ad/vente_ad/objects/<model("vente_ad.vente_ad"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vente_ad.object', {
#             'object': obj
#         })