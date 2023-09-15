from django.shortcuts import render
from django.http import HttpResponse
# from chatterbot import ChatBot

from .main_bot import chatbot

def chatbot_home(request):
    return render(request, 'index.html')


def get_response(request):
    user_input = request.GET.get('msg')
    print('=====>>>>>>', user_input)
    response = chatbot.get_response(user_input)
    print('============ "'+ str(response) + '"')
    if str(response) == "":
        return HttpResponse(str(chatbot.get_response('default_response')))
    return HttpResponse(str(response))