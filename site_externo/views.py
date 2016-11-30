from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    return render_to_response(
        'site_externo/index.html',
        locals(),
        context_instance=RequestContext(request),
        )