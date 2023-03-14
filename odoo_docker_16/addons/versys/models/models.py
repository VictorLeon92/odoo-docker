# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class Commercial(models.Model):
    _name = 'versys.commercial'
    _description = 'Commercial'

    commercial_name = fields.Char(string='Nombre del comercial')
    commercial_id = fields.Char(string='ID del comercial')
    
    client_name = fields.Selection([('C1', 'Cliente 1'), ('C2', 'Cliente 2'), ('C3', 'Cliente 3')], string='Nombre del cliente', required=True)
    client_id = fields.Char(string='ID del cliente')
    
    product = fields.Char(string='Producto a contratar')
    cost = fields.Char(string='Importe')
    payment_method = fields.Selection([('P', 'PayPal'), ('T', 'Transferencia'), ('C', 'Cheque')], string='Método de pago', required=True)
