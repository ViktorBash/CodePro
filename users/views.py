from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, InfoUpdateForm
from django.contrib.auth.decorators import login_required
import os
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login. ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required  # This makes the user be required to be logged in to see this page
def profile(request):
    if request.method == 'POST':
        # old_p_pic = request.user.profile.image.url
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, instance=request.user.profile)

        i_form =  InfoUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid and i_form.is_valid():
            u_form.save()
            p_form.save()
            i_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        i_form = InfoUpdateForm(instance=request.user.profile)

    context = {
    'i_form': i_form,
    'u_form': u_form,
    'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)
