
# from http://www.travisswicegood.com/2010/01/17/django-virtualenv-pip-and-fabric/

import django
from django.conf import settings
from django.core.management import call_command

def main():
    # Dynamically configure the Django settings with the minimum necessary to
    # get Django running tests
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.admin',
            'django.contrib.sessions',
            'multiforloop',
        ),
        # Django replaces this, but it still wants it. *shrugs*
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': '/tmp/django_login.db',
            }
        },
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'OPTIONS': {
                'debug': True,
                'string_if_invalid': 'INVALID'
            }
        }],
        MEDIA_ROOT = '/tmp/django_login_test_media/',
        ROOT_URLCONF = '',
        DEBUG = True,
    ) 
    django.setup()
    
    #call_command('syncdb')
    
    # Fire off the tests
    call_command('test', 'multiforloop')
    

if __name__ == '__main__':
    main()

