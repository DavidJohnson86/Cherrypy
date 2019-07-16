import os.path
from cherrypy import dispatch
import logging.config

logger = logging.getLogger()
db_logger = logging.getLogger('db')

LOG_CONF = {
    'version': 1,

    'formatters': {
        'void': {
            'format': ''
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'cherrypy_console': {
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'void',
            'stream': 'ext://sys.stdout'
        },
        'cherrypy_access': {
            'level':'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'void',
            'filename': 'access.log',
            'maxBytes': 10485760,
            'backupCount': 20,
            'encoding': 'utf8'
        },
        'cherrypy_error': {
            'level':'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'void',
            'filename': 'errors.log',
            'maxBytes': 10485760,
            'backupCount': 20,
            'encoding': 'utf8'
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO'
        },
        'db': {
            'handlers': ['default'],
            'level': 'INFO' ,
            'propagate': False
        },
        'cherrypy.access': {
            'handlers': ['cherrypy_access'],
            'level': 'INFO',
            'propagate': False
        },
        'cherrypy.error': {
            'handlers': ['cherrypy_console', 'cherrypy_error'],
            'level': 'INFO',
            'propagate': False
        },
    }
}

path = os.path.abspath(os.getcwd())

cherrpy_run_conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': str(path) + r'\views',
            'tools.sessions.storage_path': 'sessions',
            'tools.sessions.timeout': 10,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '',
        },
        '/contact': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '',
            },
        '/compair': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '',
            },
        '/list-view': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir':  '',
            },
        '/grid-view': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '',
            },
        '/three-col': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '',
        },
        '/four-col': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '',
        },
        '/general': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '',
        },
        '/register': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '',
        },
        '/product-details': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '',
        },


        # '/assets': {
        #     'tools.staticdir.on': True,
        #     'tools.staticdir.dir': './assets'
        # },
        #
        # '/contact': {
        #     'tools.staticdir.on': True,
        #     'tools.staticdir.dir': '../assets'
    # },

    # '/js': {
        #     'tools.staticdir.on': True,
        #     'tools.staticdir.dir': './static/js'
        # },
        # '/css': {
        #     'tools.staticdir.on': True,
        #     'tools.staticdir.dir': './static/css'
        # },
        # '/img': {
        #     'tools.staticdir.on': True,
        #     'tools.staticdir.dir': './static/img'
        # },
        # '/fonts': {
        #     'tools.staticdir.on': True,
        #     'tools.staticdir.dir': './static/fonts'}


}





# cherrpy_run_conf = {
#         '/': {
#             'tools.sessions.on': True,
#             'tools.staticdir.root': os.path.abspath(os.getcwd())},
#
#         '/logined': {
#                 'tools.sessions.on': True,
#                 'tools.staticdir.root': os.path.abspath(os.getcwd())},
#
#         '/generator': {
#             'request.dispatch': dispatch.MethodDispatcher(),
#             'tools.response_headers.on': True,
#             'tools.response_headers.headers': [('Content-Type', 'text/plain')],
#         },
#         '/public': {
#             'tools.staticdir.on': True,
#             'tools.staticdir.dir': './public',
#
#         '/protected/area': {
#             'tools.auth_basic.on': True,
#             'tools.auth_basic.realm': 'localhost',
#             'tools.auth_basic.checkpassword': VerifiedPage.LoginWebService.PUT,
#             'tools.auth_basic.accept_charset': 'UTF-8'}
#
#         }
#     }
