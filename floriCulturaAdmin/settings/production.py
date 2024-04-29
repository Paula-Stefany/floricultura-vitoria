from .settings import *

PRODUCTION_SECRET_KEY = os.getenv("PRODUCTION_SECRET_KEY")

ALLOWED_HOSTS = ['127.0.0.1']

DEBUG=False


DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
