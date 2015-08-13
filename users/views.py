from hashlib import md5
from random import random

from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponse, redirect


from users.models import PyconUser

# Create your views here.
def index(request, **kwargs):
    # import ipdb; ipdb.set_trace()
    return render(request, 'index.html')

def login(request, **kwargs):
    return render(request, 'login.html')

def signup(request, **kwargs):
    return render(request, 'signup.html')

def validate_user(request, **kwargs):
    if request.method == 'POST':
        POST = request.POST
        submit_type = POST.get('submit')
        if submit_type == 'login':
            return redirect('users:index')
        elif submit_type == 'signup':
            # TODO: validate fields
            confirm_string = md5(str(int(random()*100))).hexdigest()[:16]
            msg = ("click below to activate account \n" +
                   '127.0.0.1:8000' + reverse('users:confirm_user',
                                            kwargs={'confirm_string': confirm_string}))
            send_mail('Activate pycon account',
                      msg,
                      'Testing <testing.email.something@gmail.com>',
                      [request.POST.get('email')])
            new_user = PyconUser(email=POST['email'],
                                 username=POST['username'],
                                 confirm_string=confirm_string,
                                 password=make_password(POST['password']))
            new_user.save()
            return redirect(reverse('users:index'))
    else:
        return HttpResponse('invalid method')

def confirm_user(request, **kwargs):
    confirm_string = kwargs.get('confirm_string')
    if confirm_string:
        try:
            user = PyconUser.objects.get(confirm_string=confirm_string)
        except:
            return HttpResponse('invalid confirm_string')
        user.confirmed = True
        user.save()
        return HttpResponse(str(user))