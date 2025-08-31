# -*- coding: utf-8 -*-
{
    'name': "Custom Delivery Report",
    'version': '1.0',
    'author': "Jarosław Kopacz",
    'category': 'Inventory',
    'summary': "Rozszerzenie raportu dostawy o adres filii produkcyjnej i numer projektu klienta",
    'depends': ['stock', 'sale'],
    'data': [
        'report/report_delivery_document_inherit.xml',
        'report/report_external_layout_inherit.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}