from django.http import HttpResponse
from django.utils.timezone import datetime
import re
from django.shortcuts import render
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt

# Replace the existing home function with the one below
def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

@csrf_exempt
def send_notification(request):

    return JsonResponse({"status": 'Success'}) 