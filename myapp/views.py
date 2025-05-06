from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Profile
from django.views.decorators.csrf import csrf_exempt
import json


def welcome(request):
    return HttpResponse("welcome to first project")

def hello_world(request):
    return HttpResponse("Hello, World!")

def ProfileView(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')

        if not name or not email:
            return render(request, 'profile.html', {
                'error': 'Name and Email are required.',
                'stored_names': Profile.objects.all()
            })

        if Profile.objects.filter(name=name).exists():
            return render(request, 'profile.html', {
                'error': 'This name already exists.',
                'stored_names': Profile.objects.all()
            })

        Profile.objects.create(name=name, address=address, mobile=mobile, email=email)
        return redirect('profile')

    return render(request, 'profile.html', {'stored_names': Profile.objects.all()})


