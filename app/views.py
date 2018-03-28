from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me': "message_view"}
    return render(request, 'app/index.html', context=my_dict)


