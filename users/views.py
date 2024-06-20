from django.shortcuts import render
from .forms import SignupForm
from django.contrib import messages
from django import views
from django.contrib.auth import logout


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.add_message(request, level=200, message=f"Hi {username}! Your account is created successfully.")

    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


class LogoutView(views.View):
    def get(self, request):
        logout(request)
        return render(request, 'logout.html')



