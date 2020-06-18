from django.shortcuts import render,redirect
import os
from .forms import UserForm,UserProfileInfoForm, UserProfileInfo
from django.shortcuts import render
from django.views.generic import DetailView,UpdateView,TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth.decorators import login_required



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.
@login_required
def user_logout(request):
    #del request.session['user_id']
    request.session.flush()
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

class Aboutpageview(TemplateView):
    template_name='about.html'

class Contactpageview(TemplateView):
    template_name='contact.html'   

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

        if registered:
            return HttpResponseRedirect(reverse('user_login'))

    else:
     
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'signup.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')

        password = request.POST.get('pass')

        print(username, password)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = username
                messages.success(request, 'Signed in Sucessfully.')
                return HttpResponseRedirect(
                    reverse('detect:detector'))

               # return redirect('detect:detector')
            else:
                return HttpResponse("Account not active")
        else:
           
            
            messages.warning(request, 'Invalid Account Details Submited.')
            print(f"username: {username} and password: {password}")
            return render(request, os.path.join(BASE_DIR, "accounts/templates/home.html"), {})

    else:
        messages.info(request, 'Welcome Visitors.')

        return render(request, os.path.join(BASE_DIR, "accounts/templates/home.html"), {})

