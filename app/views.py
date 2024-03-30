from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from .form import SignupForm, LoginForm





def home(request):
    return render(request, 'index.html')

class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username, email=email, password=password)
        
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid username, email, or password")
            return super().form_invalid(form)


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
