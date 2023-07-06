# portfolio/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()

# Collect static files
if not os.getenv('DEBUG', 'True') == 'True':
    from django.core.management import call_command
    call_command('collectstatic', '--noinput')
