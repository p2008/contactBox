from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.


def all_users(request):
    return render(request, 'all_users.html')
    # return HttpResponse('asdsdd')