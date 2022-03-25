"""
WSGI config for Resi_mysql project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#For developpment mode
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Resi_mysql.settings')

#For production mode
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Resi_mysql.production')

application = get_wsgi_application()
