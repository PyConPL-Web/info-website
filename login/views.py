from django.contrib.auth import authenticate, login
from django.shortcuts import render

from users.models import User


def index(request):
    if request.method == 'GET':
        # render login form
        pass
    elif request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(username=username, password=passwd)
        if user is None:
            # TODO: return bad password
            pass
        login(request, user)
        # TODO: redirect to the main page
        pass
