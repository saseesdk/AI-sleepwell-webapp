from django.shortcuts import redirect, render
from django.contrib.auth import logout
# Create your views here.
def login(request):
    return render(request,'home.html')

def logout(request):
    logout(request)
    # Redirect to the login page or any other page after logout
    return render(request, 'login_signup.html')

