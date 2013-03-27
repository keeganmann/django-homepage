from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
# Create your views here.

def contact(request, template='contact.html'):
    """Displays a contact form."""
    response = render_to_response(template, RequestContext(request))
    return response


def home(request):
    variables = RequestContext(request, {})
    response = render_to_response('index.html', variables)
    return response
    