from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render
from models import ButtonUsage

def chat(request): 
    #context = {}   
    ButtonUsage.objects.create(
        stupidButton=0,
        fatButton=0,
        dumbButton=0
    )
    UserID = ButtonUsage.objects.all().order_by("-User")[0].User
    context = {'UserID' : UserID}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }  

    result_message = {
        'type': 'text'
    }
    if 'fat' in message['text']:
        result_message['text'] = random.choice(jokes['fat'])
        userID = ButtonUsage.objects.all().order_by("-User")[0].User
        count = ButtonUsage.objects.all().order_by("-User")[0].fatButton
        ButtonUsage.objects.filter(User=userID).update(fatButton=count+1)
    
    elif 'stupid' in message['text']:
        result_message['text'] = random.choice(jokes['stupid'])
        userID = ButtonUsage.objects.all().order_by("-User")[0].User
        count = ButtonUsage.objects.all().order_by("-User")[0].stupidButton
        ButtonUsage.objects.filter(User=userID).update(stupidButton=count+1)
    
    elif 'dumb' in message['text']:
        result_message['text'] = random.choice(jokes['dumb'])
        userID = ButtonUsage.objects.all().order_by("-User")[0].User
        count = ButtonUsage.objects.all().order_by("-User")[0].dumbButton
        ButtonUsage.objects.filter(User=userID).update(dumbButton=count+1)

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you! If you're interested in yo mama jokes, just click the fat, stupid or dumb button and i'll tell you an appropriate joke."
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    return result_message

def usage(request):
    btusage = ButtonUsage.objects.order_by("User")
    return render(request, 'chatbot_tutorial/usage.html', { 'btusage':btusage })
    