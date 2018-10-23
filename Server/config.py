from datetime import timedelta
import os


class Config:
    SERVICE_NAME = 'fridge_manager'

    RUN_SETTING = {
        'host': 'localhost',
        'port': 5000,
        'debug': True,
        'threaded': True
    }
    # uWSGI를 통해 배포되어야 하므로, production level에선 run setting을 건드리지 않음

    SECRET_KEY = os.getenv('SECRET_KEY', '85c145a16bd6f6e1f3e104ca78c6a102')

    # production level 에서 기간 조정
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)
    JWT_HEADER_TYPE = 'JWT'

    MONGODB_SETTING = {
        'db': SERVICE_NAME,
        'host': 'localhost',
        'port': 27017
    }

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': '"Fridge Manager" API',
            'version': '1.0',
            'description': ''
        },
        'host': '', # TODO
        'basePath': '/ '
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Some Tag',
                'description': 'Some API'
            },
        ]
    }


class LocalDBConfig:
    MONGODB_SETTINGS = {
        'host': 'localhost',
        'port': 27017,
        'db': Config.SERVICE_NAME
    }


class RemoteDBConfig:
    pass
