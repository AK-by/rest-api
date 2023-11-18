import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lessons.settings')
application = get_asgi_application()

# https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
# Обеспечивает подключение к серверу
