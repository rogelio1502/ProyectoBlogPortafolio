from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['djangored.herokuapp.com',"localhost"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2h3n5pakkup4u',
        'USER':'ayydxznbdwlzcs',
        'PASSWORD':'f9c9c336d4b20ad0254328a6d929dd56394e6814c30ecfe19b20d566440835fb',
        'HOST':'ec2-34-194-130-103.compute-1.amazonaws.com',
        'PORT':'5432'
    }
}
