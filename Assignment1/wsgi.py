"""
WSGI config for Assignment1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys, site



CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
WORK_DIRECTORY = os.path.join(CURRENT_DIRECTORY, '..')
site.addsitedir('/opt/python/run/venv/lib/python2.7/site-packages')
site.addsitedir('/usr/local/lib/python2.7/site-packages')
os.environ["DJANGO_SETTINGS_MODULE"] = "Assignment1.settings"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
