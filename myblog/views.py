import logging

from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect, Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from articles.models import Article, Tag
from datetime import datetime

def home(request):
    variables = RequestContext(request, {})
    response = render_to_response('index.html', variables)
    return response


