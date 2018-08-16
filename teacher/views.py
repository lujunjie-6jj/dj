from django.shortcuts import render
from django.http import HttpResponse

from django.core.urlresolvers import reverse
# Create your views here.

def normalamb(request):
    return HttpResponse('游子阿  ！！！！！！！！！！')

def withparam(request,year,month):
    return HttpResponse('this is withparam {0},{1}'.format(year,month))

def ljj(request):
    return HttpResponse('woshilujunjie!')

def param(request,pn):
    return HttpResponse('page number is {0}'.format(pn))

def name(request,name):
    return HttpResponse("my name is {0}".format(name))

def wangshi(r):
    return HttpResponse("your request url is {0}".format(reverse))