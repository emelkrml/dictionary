from django.contrib.auth.models import User
from login.models import UserForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template import RequestContext

def register(request):
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
                uform = UserForm(data = request.POST)
                if uform.is_valid():
                        user = uform.save()
                        # form brings back a plain text string, not an encrypted password
                        pw = user.password
                        # thus we need to use set password to encrypt the password string
                        user.set_password(pw)
                        user.save()

                        registered = True
                else:
                        print(uform.errors)
        else:
                uform = UserForm()

        return render(request, 'login/register.html', {'uform': uform,  'registered': registered }, context)


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect("login/")
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print ("invalid login details " + username + " " + password)
              return render(request, 'login/login.html', {}, context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'login/login.html', {}, context)
