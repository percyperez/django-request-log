"""
Use for testing on sqlite3...

$ ./manage.py test
"""
PROJECT_NAME = 'request-log'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/test.db',
        'USER': PROJECT_NAME,
        'PASSWORD': PROJECT_NAME,
        'HOST': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'log',
    'django_nose'
)

NOSE_ARGS = [
    '--logging-clear-handlers',
    '--with-progressive',
    '-s',
]
SECRET_KEY = '&6hr-f+2+5k!$-oq6*l7p79+^+txtckz7imdoi%!a&0h1t3d(@'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'