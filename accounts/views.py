from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
     
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password."}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return render(request, 'add_lab_processing.html', {})

    return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'accounts/login.html', {})
        
    return render(request, 'accounts/logout.html', {})

