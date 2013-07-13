from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from models import homepageFeature
from django.conf import settings
# Create your views here.

def contact(request, template='contact.html'):
    """Displays a contact form."""
    response = render_to_response(template, RequestContext(request, {'FOXYFORM_URL': settings.FOXYFORM_URL}))
    return response


def home(request):
    variables = RequestContext(request, {"features": homepageFeature.objects.order_by('ordering').all()})
    response = render_to_response('index.html', variables)
    return response
    