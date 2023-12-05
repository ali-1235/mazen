{
    'name': '17',
    'summary': '',
    'description': " ",
    'author': 'mazen',
    'website': '',

    # category can be used to filter modules in modules listing
    'category': 'test',
    'version': '0.1',

    # any module for this one to work correctly
    'depends': ['base'],
   
    # always loaded
    'data': [
            'security/ir.model.access.csv',
            'views/about_us.xml',
            'views/hero.xml',
            'views/values.xml',
            'views/partner.xml',
            'views/home.xml',
            'views/leaderShip.xml',
            'data/about_us.xml',
            'views/contact_us.xml',
            'views/Blog.xml',
            'views/case_study.xml',
            'views/news.xml'
            
            
    ],


    # loaded in demo mode only
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    
    }
