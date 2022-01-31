"""
WSGI config for mg_tourism project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys

# add the virtualenv site-packages path to the sys.path
site_packages = '/home/thinkland/projects/envs/mg_tourism_env/lib/python3.10/site-packages'
if site_packages not in sys.path:
    sys.path.append(site_packages)

project_path = '/home/thinkland/projects/mg_tourism'
project_path2 = '/home/thinkland/projects/mg_tourism/mg_tourism'

if project_path not in sys.path:
    sys.path.append(project_path)
if project_path2 not in sys.path:
    sys.path.append(project_path2)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mg_tourism.settings')

application = get_wsgi_application()
