from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import User

@login_required
def index(request):
    # TODO: manage your account - password etc 
    pass


def activate(request, activation_string):
    user = get_object_or_404(User, activation_string=activation_string)
    if user != request.user:
        # TODO: raise permission denied
        pass
    if not user.is_active:
        user.is_active = True
        user.save()
    if not request.user.is_authenticated():
        # TODO: authenticate user
        pass
    # TODO: redirect to homepage


    # login is not required, and if you are not logged in, then
    # you will be logged in, if you are currently loggedin you will be 
    # redirected to the main page.
    # if your account is active, you will be redirected to main page instead of
    # being re-activated and logged (to prevent brute-force logging by 
    # activating other's ures account)

