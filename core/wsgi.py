import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()

# https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
# Обеспечивает подключение к серверу
