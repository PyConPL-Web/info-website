from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    if request.method == 'GET':
        return render(request, 'login/index.html')
    elif request.method == 'POST':
        uname = request.POST['username']
        pas = request.POST['password']
        user = authenticate(username=uname, password=pas)
        if user is None:
            return render(request, 'login/index.html', context={
                'bad_password': 1
            })
        else:
            login(request, user)
            # redirect to mainpage
            # return redirect()
            return HttpResponse('zalogowany')
