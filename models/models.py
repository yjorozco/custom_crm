# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
     _name = 'custom_crm.visit'
     _description = 'Visit'

     name = fields.Char(string='Descripcion')
     customer = fields.Char(string='Cliente')
     date = fields.Datetime(string='Fecha')
     type = fields.Selection([('p','Presencial'),('m', 'WhatsApp'),('T', 'Telefonico')], string='Tipo', required=True)
     done = fields.Boolean(string='Realizada', readonly=True)

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
