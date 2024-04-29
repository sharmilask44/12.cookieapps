from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def input(request):
    return render(request,'base.html')
def add(request):
    x=int(request.GET['t1'])
    y=int(request.GET['t2'])
    z=x+y
    resp=HttpResponse('values submitted successfully')
    resp.set_cookie('z',z,max_age=100)
    return resp
def display(request):
    if 'z' in request.COOKIES:
        sum=request.COOKIES['z']
        return HttpResponse("addition of two numbers:"+sum)
    else:
        return HttpResponse("pls enter values")

# Create your views here.
