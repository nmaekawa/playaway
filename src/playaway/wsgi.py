"""
WSGI config for playaway project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

from dotenv import load_dotenv
import os

from django.core.wsgi import get_wsgi_application

# if dotenv file, load it
dotenv_path = None
if 'PLAYAWAY_DOTENV_PATH' in os.environ:
    dotenv_path = os.environ['PLAYAWAY_DOTENV_PATH']
elif os.path.exists(os.path.join('playaway', 'settings', '.env')):
    dotenv_path = os.path.join('playaway', 'settings', '.env')
if dotenv_path:
    load_dotenv(dotenv_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playaway.settings.base")

application = get_wsgi_application()
