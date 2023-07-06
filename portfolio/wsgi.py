# portfolio/wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise  # new
from django.conf import settings  # new

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=str(settings.BASE_DIR / 'staticfiles'))  # modified
