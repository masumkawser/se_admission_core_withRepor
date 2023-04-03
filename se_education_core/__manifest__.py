# -*- coding: utf-8 -*-
{
    'name': "SmartEdu Core",
    'summary': 'Manage Students, Faculties and Education Institute',
    'author': "DSL",
    'category': 'Education',
    'version': '0.1',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        # security
        'security/ir.model.access.csv',
        # views
        'views/se_student_view.xml',
        'views/se_course_view.xml',
        'views/se_address_type_view.xml',
        'views/se_department_view.xml',
        'views/se_subject_view.xml',
        'views/se_batch_view.xml',
        'views/menus.xml',
    ],
}
