from django.http import HttpResponse
from django.template import loader
from .models import Users

def index(request):
  myusers = Users.objects.all().values()
  output =""
  for x in myusers:
    output += x["firstname"]
  return HttpResponse(output)
