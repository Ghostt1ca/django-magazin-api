import os
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Aceasta linie ruleaza migrarile la fiecare pornire de proces
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Migration failed: {e}")

application = get_wsgi_application()