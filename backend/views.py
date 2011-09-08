# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from pants.models import Pant, Item
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def allpants(request):
    pant_list = Item.objects.all()[:16]
    return render_to_response('backend/all.html', {'pant_list': pant_list})

def sameW(request):
    pant_list = Item.objects.filter(waist="Same waist")
    return render_to_response('backend/sameW.html', {'pant_list': pant_list})

def tighterW(request):
    pant_list = Item.objects.filter(waist="Tighter waist")
    return render_to_response('backend/tighterW.html', {'pant_list': pant_list})

def looserW(request):
    pant_list =Item.objects.filter(waist="Looser waist")
    return render_to_response('backend/looserW.html', {'pant_list': pant_list})

def sameR(request):
    pant_list =Item.objects.filter(rise="Same rise")
    return render_to_response('backend/sameR.html', {'pant_list': pant_list})

def lowerR(request):
    pant_list =Item.objects.filter(rise="Lower rise")
    return render_to_response('backend/lowerR.html', {'pant_list': pant_list})

def higherR(request):
    pant_list =Item.objects.filter(rise="Higher rise")
    return render_to_response('backend/higherR.html', {'pant_list': pant_list})

def slim(request):
    return HttpResponse("thanks")

