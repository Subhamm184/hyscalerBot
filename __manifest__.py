{
    'name': 'Chatbot Recruitment',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Chatbot for company recruitment and application',
    'depends': ['base', 'web', 'hr'],
    'data': [
        'views/chatbot_user_views.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
