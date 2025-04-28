from django.http import HttpResponse

def welcome(request):
    return HttpResponse("welcome to first project")

def hello_world(request):
    return HttpResponse("Hello, World!")

# Create your views here.
