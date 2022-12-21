# -*- coding: utf-8 -*-

{
    'name': 'Sale order line menu with cancel motif field',
    'version': '1.0.1.1',
    'author':'Soft-integration',
    'category': 'Sale',
    'description': "",
    'depends': [
        'sale_order_line_menu','stock_picking_order_line_cancel_motif'
    ],
    'data': [
        'views/sale_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
