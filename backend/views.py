# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from pants.models import Pant, Item
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def prototypeA(request):
    search_query = request.GET['searchpant']
    pant_list = Item.objects.all().order_by('similarity')
    t_data = dict()
    t_data['pant_list'] = pant_list
    
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/prototypeA.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey, 'search_query': search_query})

@login_required
def sameW(request):
    pant_list = Item.objects.filter(waist="Same waist")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/sameW.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def tighterW(request):
    pant_list = Item.objects.filter(waist="Tighter waist")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/tighterW.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})
 

def looserW(request):
    pant_list =Item.objects.filter(waist="Looser waist")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/looserW.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})
   
@login_required
def sameR(request):
    pant_list =Item.objects.filter(rise="Same rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/sameR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def lowerR(request):
    pant_list =Item.objects.filter(rise="Lower rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/lowerR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def higherR(request):
    pant_list =Item.objects.filter(rise="Higher rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/higherR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def sWsR(request):
    pant_list =Item.objects.filter(rise="Same rise", waist="Same waist")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/combos/sWsR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def sWlR(request):
    pant_list =Item.objects.filter(waist ="Same waist", rise="Lower rise")
    pant_list =Item.objects.filter(rise="Lower rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/combos/sWlR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})


def sWhR(request):
    pant_list =Item.objects.filter(waist="Same waist", rise="Higher rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/combos/sWhR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def tWsR(request):
    pant_list =Item.objects.filter(waist="Tighter waist", rise="Same rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/combos/tWsR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def tWhR(request):
    pant_list =Item.objects.filter(waist="Tighter waist", rise="Higher rise")
    pant_list =Item.objects.filter(rise="Lower rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/combos/tWhR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def tWlR(request):
    pant_list =Item.objects.filter(waist="Tighter waist", rise="Lower rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/combos/tWlR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def lWsR(request):
    pant_list =Item.objects.filter(waist="Looser waist", rise="Same rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/combos/lWsR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def lWlR(request):
    pant_list =Item.objects.filter(waist="Looser waist", rise="Lower rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/combos/lWlR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def lWhR(request):
    pant_list =Item.objects.filter(waist="Looser waist", rise="Higher rise")
    sale = Item.objects.filter(sale="$65.00")
    color = Item.objects.filter(color1="brown.jpg")
    khaki = Item.objects.filter(color2="khaki.jpg")
    red = Item.objects.filter(color3="red.jpg")
    grey = Item.objects.filter(color4="grey.jpg")
    return render_to_response('backend/combos/combos/lWhR.html', {'pant_list': pant_list, 'sale': sale, 'color': color, 'khaki': khaki, 'red': red, 'grey': grey})

@login_required
def slim(request):
    return HttpResponse("thanks")

