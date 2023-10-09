#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloproject.settings')
    try:
        from django.core.management import execute_from_command_line
        from django.core.management.commands.runserver import Command as runserver
        runserver.default_port = os.environ.get('PORT', '8080')
        runserver.default_addr = '0.0.0.0'
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
web: python3 -m ptvsd --port 3000 --host 0.0.0.0 manage.py runserver 0.0.0.0:8080 --noreload
source /Users/webtechnicom/PycharmProjects/venv/bin/activate
(base) webtechnicom@MacBook-Pro-de-steve hello-world-2 % source /Users/webtechnicom/PycharmP
rojects/venv/bin/activate
(venv) (base) webtechnicom@MacBook-Pro-de-steve hello-world-2 % >....                       
        echo "Expected content found -- site is up"
        echo "END CONTENT TEST: Success! ✅"