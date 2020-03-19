#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from dotenv import load_dotenv
import os
import sys


def main():
    # if dotenv file, load it
    dotenv_path = None
    if 'PLAYAWAY_DOTENV_PATH' in os.environ:
        dotenv_path = os.environ['PLAYAWAY_DOTENV_PATH']
    elif os.path.exists(os.path.join('src', 'playaway', 'settings', '.env')):
        dotenv_path = os.path.join('src', 'playaway', 'settings', '.env')
    if dotenv_path:
        load_dotenv(dotenv_path)

    # define settings if not in environment
    if os.environ.get("DJANGO_SETTINGS_MODULE", None) is None:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playaway.settings.dev")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
