from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request

from .models import Place, Guide


# Create your views here.
def frontpage(request):
    obj=Place.objects.all()
    gobj=Guide.objects.all()
    return render(request,'index.html',{'result':obj,'gresult':gobj})


