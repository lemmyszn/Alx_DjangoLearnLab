# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView

class UserLoginView(LoginView):
    template_name = 'blog/login.html'

class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'

from django.shortcuts import render , redirect 
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

