# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from pants.models import Pant
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def inquiry(request):
    return HttpResponse("Working!")

def login_view(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_view(request):
    return render_to_response('logout.html', context_instance=RequestContext(request))

def logout_action(request):
    logout(request)
    return HttpResponse("Successfully logged out!")

def log_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('loggedin.html')
        else: 
            return HttpResponse("You're out!")
    else: 
        return HttpResponse("None")

@login_required
def search(request):
    return render_to_response('search.html')

@login_required
def dynamiccatalog(request):
    return render_to_response('dynamiccatalog.html')

@login_required(login_url='/')
def about(request):
    return render_to_response('about.html')

@login_required(login_url='/')
def aboutstaff(request):
    return render_to_response('aboutstaff.html')

@login_required(login_url='/')
def press(request):
    return render_to_response('press.html')

@login_required(login_url='/')
def findus(request):
    return render_to_response('findus.html')

def submit(request, pant_id):
    p = get_object_or_404(Pant, pk=pant_id)
    p.waist = request.POST['waist']
    p.front_rise = request.POST['front_rise']
    p.back_rise = request.POST['back_rise']
    p.leg_opening = request.POST['leg_opening']
    p.in_seam = request.POST['in_seam']
    p.out_seam = request.POST['out_seam']
    p.brand = request.POST['brand']
    p.style = request.POST['style']
    p.save()
    return HttpResponse("Thanks!")

def detail(request, pant_id):
    p = get_object_or_404(Pant, pk=pant_id)
    return render_to_response('detail.html', {'pant': p},
                              context_instance=RequestContext(request))

def thanks(request):
    return render_to_response('basetwo.html')
