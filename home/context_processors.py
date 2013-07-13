from django.conf import settings
from django.contrib.sites.models import get_current_site
from models import NavItem, HeaderImage

def site(request):
    return {'SITE_NAME': get_current_site(request).name}

def navbar(request):
    return {'NAV_ITEMS': NavItem.objects.order_by('ordering').all()}

class HeaderImageMiddleware(object):  
    def process_view(self, request, view_func, view_args, view_kwargs):  
        viewheaders = HeaderImage.objects.filter(view_name=view_func.__name__).order_by('?')
        if len(viewheaders) > 0:
            header = viewheaders[0]
        else:
        	try:
            	header = HeaderImage.objects.filter(view_name="").order_by('?')[0]
            except IndexError as e:
            	request.HEADER_IMAGE_URL = ""
            	return
        request.HEADER_IMAGE_URL = header.imgurl

def headerimage(request):
	return {'HEADER_IMAGE_URL': request.HEADER_IMAGE_URL}
