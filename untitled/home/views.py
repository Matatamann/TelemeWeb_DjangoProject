from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index( request ):
    return render_to_response('home/index.html', context_instance=RequestContext(request))

def rpm( request ):
    return render_to_response('home/rpm.html', context_instance=RequestContext(request))

def velocity( request ):
    return render_to_response('home/velocity.html', context_instance=RequestContext(request))

def gps( request ):
    return render_to_response('home/gps.html', context_instance=RequestContext(request))

def fuel( request ):
    return render_to_response('home/fuel.html', context_instance=RequestContext(request))

def temperature( request ):
    return render_to_response('home/temperature.html', context_instance=RequestContext(request))

def positions( request ):
    return render_to_response('home/positions.html', context_instance=RequestContext(request))

def trail( request ):
    return render_to_response('home/trail.html', context_instance=RequestContext(request))

def developer( request ):
    return render_to_response('home/developer.html', context_instance=RequestContext(request))
