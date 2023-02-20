# -*- coding: utf-8 -*- 


{
 'name': 'Manufacturing order with editable finished date',
 'author': 'Soft-integration',
 'application': False,
 'installable': True,
 'auto_install': False,
 'qweb': [],
 'description': False,
 'images': [],
 'version': '1.0.1.1',
 'category': 'Manufacturing/Manufacturing',
 'demo': [],
 'depends': ['mrp'],
 'data': [
     'security/mrp_production_order_date_finished_editable_security.xml',
     'views/mrp_production_views.xml',
    ],
 'license': 'LGPL-3',
 }