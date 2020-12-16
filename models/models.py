# -*- coding: utf-8 -*-

from odoo import models, fields, api

class soportes(models.Model):   
    _inherit = ['mail.thread', 'mail.activity.mixin'] 
    _name = 'soportes.soportes'
    _description = 'soportes.soportes'
    _rec_name='tipo_solicitud'

    fecha_solicitud = fields.Date(string="Fecha de solicitud", default=fields.Date.today)
    descripcion = fields.Text(String="Descripción del soporte")
    tipo_solicitud = fields.Selection([
        ('1', 'Solicitud de acceso y privilegios'),
        ('2', 'Solicitud de cambios'),        
        ('3', 'Solicitud de compra'),
        ('4', 'Solicitud de correo electrónico'),
        ('5', 'Solicitud de desarrollo'),
        ('6', 'Solicitud de equipo de cómputo'),
        ('7', 'Solicitud de información y asesoría'),
        ('8', 'Solicitud de infraestructura de red'),
        ('9', 'Incidente de sistema'),
        ('10', 'Incidente de correo electrónico'),
        ('11', 'Incidente de equipo de cómputo'),
        ('12', 'Incidente de infraestructura de red'),
        ('13', 'Incidente de internet'),
        ('14', 'Incidente de servidores'),
        ('15', 'Incidente de suministro el eléctrico'),
        ('16', 'Incidente de seguridad'),
        ('17', 'Quejas')], default='1', String="Tipo de solicitud")
    imagen = fields.Binary(String="Archivo adjunto")
