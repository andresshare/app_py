from django.shortcuts import render
from django.http import HttpResponse
from app.models import Topic, Webpage, AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dict = {'insert_me': "message_view"}
    return render(request, 'app/index.html', context=date_dict)

