"""
WSGI config for helloproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloproject.settings')

application = get_wsgi_application()
web: python3 -m ptvsd --port 3000 --host 0.0.0.0 manage.py runserver 0.0.0.0:8080 --noreload
source /Users/webtechnicom/PycharmProjects/venv/bin/activate
(base) webtechnicom@MacBook-Pro-de-steve hello-world-2 % source /Users/webtechnicom/PycharmP
rojects/venv/bin/activate
(venv) (base) webtechnicom@MacBook-Pro-de-steve hello-world-2 % >....                       
        echo "Expected content found -- site is up"
        echo "END CONTENT TEST: Success! ✅"