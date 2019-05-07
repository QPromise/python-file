LOGGING_CONFIG = {
    'version' : 1,
    'handlers' : {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simpleFormatter'
        }
    },
    'formatters': {
        'simpleFormatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'loggers' : {
        'simple_example' : {
            'level' : 'DEBUG',
            'handlers' : ['console']
        }
    }
}