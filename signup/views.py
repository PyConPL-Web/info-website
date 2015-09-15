from datetime import datetime
from hashlib import md5

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request,* args, **kwargs):
    if request.method == 'GET':
        return render(request, 'signup/index.html')
    elif request.method == 'POST':
        POST = request.POST
        confirm_string = md5(str(datetime.utcnow())).hexdigest()[:16]
        msg = ("click below to activate account \n" +
                   '127.0.0.1:8000' + reverse('users:confirm_user',
                                        kwargs={'confirm_string': confirm_string}))
            send_mail('Activate pycon account',
                      msg,
                      'Testing <testing.email.something@gmail.com>',
                      [request.POST.get('email')])
            # new_user = PyconUser(email=POST['email'],
            #                      username=POST['username'],
            #                      confirm_string=confirm_string)
            # new_user.save()
            return render(request, 'sugnup/index.html', context={
                'confirm': 1
            })


def confirm(request, *args, **kwargs):
    confirm_string = kwargs.get('confirm_string')
    if confirm_string:
        try:
            # user = PyconUser.objects.get(confirm_string=confirm_string)
        except:
            return HttpResponse('invalid confirm_string')
        user.is_confirmed = True
        user.save()
        # redirect to manpage
        # return HttpResponse(str(user))