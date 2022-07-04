from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Users

def index(request):
  myusers = Users.objects.all().values()
  template = loader.get_template('index.html')
  context ={
    'myusers': myusers,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  user = Users (firstname=x, lastname=y)
  user.save()
  return HttpResponseRedirect(reverse('index'))