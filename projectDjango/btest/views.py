from django.shortcuts import render

# Create your views here.
from .models import *



def index(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, "btest/index.html", {'bbs1': bbs})

