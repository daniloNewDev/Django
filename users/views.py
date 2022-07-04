from django.http import HttpResponse
from django.template import loader
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