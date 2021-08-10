from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['djangored.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd59v3pqv2kf0tm',
        'USER':'yxbotbxczvocdy',
        'PASSWORD':'2a8c6dc3d312157ac1800b37ef830e7742c51a635434de16878d2e715893fdc8',
        'HOST':'ec2-3-218-149-60.compute-1.amazonaws.com',
        'PORT':'5432'
    }
}
