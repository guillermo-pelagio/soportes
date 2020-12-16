# -*- coding: utf-8 -*-
{
    'name': "Tickets sistemas",
    'summary': "Módulo para reportar incidentes/solicitudes del sistema",
    'description': "Módulo para reportar incidentes/solicitudes del sistema",
    
    'author': "Guillermo Pelagio",
    'website': "http://www.barmex.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '20.12.10',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}