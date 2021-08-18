from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['djangored.herokuapp.com',"*"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME'),
        'USER':os.getenv('USER'),
        'PASSWORD':os.getenv('PASSWORD'),
        'HOST':os.getenv('HOST'),
        'PORT':'5432'
    }
}
