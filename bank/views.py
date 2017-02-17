# Create your views here.
# importing the necessary packages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext


# function for opening bank homepage
# enforcing that anyone accessing must be logged in using login_required function


@login_required
def home(request):
    return render(request, 'bank/home/index.html')


def selfCheck(request):
    # checks if the incoming request is from a user who is authenticated before redirecting to the bank homepage
    context = RequestContext(request)

    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        return render(request, 'users/sign.html', context)


def signin(request):
    # Get the next where after successful sign in will be redirected to
    next = request.GET.get('next', '/')
    # Boolean for showing/hiding error messages
    invalidLogin = False
    # Obtain the context for the user's request.
    context = RequestContext(request)
    #     For now, we shall only allow login, later will add the signup part
    if request.POST:
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)

                return HttpResponseRedirect(next)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            invalidLogin = True
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response('users/sign.html', {'failed': invalidLogin}, context)

            # The request is not a HTTP POST, so display the login form.
            # This scenario would most likely be a HTTP GET.
    else:

        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('users/sign.html', {'failed': invalidLogin}, context)


@login_required
def sign_out(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')