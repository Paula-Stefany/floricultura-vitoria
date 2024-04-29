from .settings import *


DEBUG = True 

ALLOWED_HOSTS = ['127.0.0.1']

TESTING_SECRET_KEY = os.getenv("TESTING_SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
