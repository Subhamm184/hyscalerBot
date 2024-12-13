{
    'name': 'Recruitment Chatbot',
    'version': '1.1',
    'category': 'Utility',
    'summary': 'Interactive Chatbot for Recruitment Processes',
    'depends': ['base', 'web', 'hr'],
    'data': [
        'views/chatbot_user_interface.xml',
        'data/sample_data.xml', 
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
