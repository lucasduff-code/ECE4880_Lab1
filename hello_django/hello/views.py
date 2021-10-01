from django.http import HttpResponse
from django.utils.timezone import datetime
import re
from django.shortcuts import render #, render_to_response
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import os
from twilio.rest import Client

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
def send_notification(request, to_num, notif_message, limit, unit):

    account_sid = os.environ['TWILIO_ACCOUNT_SID'] 
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] 
    client = Client(account_sid, auth_token)

    send_body = 'The temperature has exceeded the ' + notif_message + ' limit of ' + limit + ' ' + unit

    message = client.messages \
                    .create(
                        body= send_body, #"Good morning Brogrammers!",
                        from_='+15052278737',
                        to= to_num #'+15635439088'
                    )

    # print(message.sid)

    # print('SENT MESSAGE!')


    return HttpResponse(status=200)  #JsonResponse({"status": 'Sent notification to: '}) 