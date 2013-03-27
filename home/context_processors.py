from django.conf import settings
from django.contrib.sites.models import get_current_site
from models import NavItem

def site(request):
    return {'SITE_NAME': get_current_site(request).name}

def navbar(request):
    return {'NAV_ITEMS': NavItem.objects.all()}
