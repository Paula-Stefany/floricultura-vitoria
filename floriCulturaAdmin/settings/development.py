from .settings import *

DEBUG=True

DEVELOPMENT_SECRET_KEY = os.getenv("DEVELOPMENT_SECRET_KEY")

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}