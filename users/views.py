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

def delete(request, id):
  user = Users.objects.get(id=id)
  user.delete()
  return HttpResponseRedirect(reverse(index))

def update(request, id):
  myuser = Users.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'myuser': myuser,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  user = Users.objects.get(id=id)
  user.firstname = first
  user.lastname = last
  user.save()
  return HttpResponseRedirect(reverse('index'))