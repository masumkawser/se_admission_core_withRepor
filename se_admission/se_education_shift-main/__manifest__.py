# -*- coding: utf-8 -*-
{
    'name': "SmartEdu Education Shift",
    'summary': 'Education Shift Management System.',
    'description': 'Education Shift Management System',
    'author': "DSL",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base',
                'se_education_core',
                ],
    'data': [
        # security
        'security/ir.model.access.csv',
        # views
        'views/se_education_shift_views.xml',
        'views/menus.xml',
    ],
    'demo': [],
}
