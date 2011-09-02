# Create your views here.                                                                                                               

from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from pants.models import Pant
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def results(request):
    return render_to_response('results.html')

@login_required
def tighterWtighterA(request):
    return render_to_response('318.html')

@login_required
def tighterWsameA(request):
    return render_to_response('319.html')

@login_required
def tighterWlooserA(request):
    return render_to_response('3110.html')

@login_required
def sameWlooserA(request):
    return render_to_response('3210.html')
@login_required
def sameWsameA(request):
    return render_to_response('329.html')

@login_required
def sameWtighterA(request):
    return render_to_response('328.html')

@login_required
def looserWlooserA(request):
    return render_to_response('3310.html')

@login_required
def looserWsameA(request):
    return render_to_response('339.html')

@login_required
def looserWtighterA(request):
    return render_to_response('338.html')


@login_required
def oneten(request):
    return render_to_response('110.html')

@login_required
def oneeleven(request):
    return render_to_response('111.html')

@login_required
def onetwelve(request):
    return render_to_response('112.html')

@login_required
def twelve(request):
    return render_to_response('twelve.html')

@login_required
def thirteen(request):
    return render_to_response('thirteen.html')

@login_required
def fourteen(request):
    return render_to_response('fourteen.html')

@login_required
def fifteen(request):
    return render_to_response('fifteen.html')

@login_required
def ninethirtytwo(request):
    return render_to_response('nine32.html')

@login_required
def ninethirtyone(request):
    return render_to_response('nine31.html')

@login_required
def ninethirtythree(request):
    return render_to_response('nine33.html')

@login_required
def eight(request):
    return render_to_response('eight.html')

@login_required
def nine(request):
    return render_to_response('nine.html')

@login_required
def ten(request):
    return render_to_response('ten.html')

@login_required
def thirtytwo(request):
    return render_to_response('thirtytwo.html')

@login_required
def thirtythree(request):
    return render_to_response('thirtythree.html')

@login_required
def thirtyone(request):
    return render_to_response('thirtyone.html')
