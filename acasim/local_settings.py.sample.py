from django.conf import settings
DEBUG = True
ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'academy',
        'USER': "postgres",
        'PASSWORD': "xcWI3128",
        'PORT': 5432
    }
}