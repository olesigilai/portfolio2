from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
# Create your views here.
def home (request):
    return render(request, 'index.html')