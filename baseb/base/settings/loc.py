from base.settings.default import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pureye4u',
        'USER': 'pureye4u',
        'PASSWORD': 'audtjs77',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
