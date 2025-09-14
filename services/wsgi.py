import os
import sys # New import

from django.core.wsgi import get_wsgi_application

# Add your project directory to the sys.path
path = '/opt/render/project/src/services' # This is a common path on Render for the project root
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'services.settings')

application = get_wsgi_application()