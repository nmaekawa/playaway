from .base import *

# test db is sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'hxat-test-sqlite3.db'),
    },
}

