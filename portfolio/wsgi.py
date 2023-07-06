# portfolio/wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise  # new

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=str(BASE_DIR / 'staticfiles'))  # new

