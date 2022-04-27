from django.http import HttpResponse
from django.shortcuts import render
from . models import Leaders
# Create your views here.
def demo(request):
    obj=Leaders.objects.all()
    return render(request,"index.html",{'result':obj})
