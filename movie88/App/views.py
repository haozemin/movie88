from django.shortcuts import render
from App.models import *

# Create your views here.
def index(request):
    bcs = Category.objects.filter(parentid=0)
    scs = Category.objects.filter(parentid__gt=0)
    return render(request,'app/index.html',locals())