# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from pants.models import Pant, Item
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def shuffle(request):
    import random
    num_pants = len(Item.objects.all())
    j = random.randrange(0, num_pants)
    k = random.randrange(0, num_pants)
    l = random.randrange(0, num_pants)
    m = random.randrange(0, num_pants)
    pant_list = Item.objects.filter(pk__in=[j, k, l, m])
    return render_to_response('shuffle/shuffle.html', {'pant_list': pant_list})


