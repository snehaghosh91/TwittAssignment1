"""
WSGI config for Assignment1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import site
import sys

# Remember original sys.path.
prev_sys_path = list(sys.path) 

# we add currently directory to path and change to it
pwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(pwd)
sys.path = [pwd] + sys.path

# find the site-packages within the local virtualenv
for python_dir in os.listdir('lib'):
    site_packages_dir = os.path.join('lib', python_dir, 'site-packages')
    if os.path.exists(site_packages_dir):
        site.addsitedir(os.path.abspath(site_packages_dir))

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ["DJANGO_SETTINGS_MODULE"] = "Assignment1.settings"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
