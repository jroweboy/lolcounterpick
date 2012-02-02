from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotModified

def index(request):
    return render(request, 'index.html')