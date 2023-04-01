from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from users.models import CustomUser


def users(request):
    return HttpResponse("Try the following<br> - users/login<br> - users/signin ")


def registerUser(request, type, type_file):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, password=password)
        newUser = CustomUser()
        newUser.user = user

        # Asssigning "Type" to the User
        newUser.userType = type
        # Saving The User Models
        newUser.save()

        return redirect("login")
        # return render(request, 'home.html', {'response':"you are a Client"})
        
    return render(request, type_file)

def RegisterClient(request):
    return registerUser(request, "client", 'register_client.html')
def RegisterShop(request):
    return registerUser(request, "repair shop", 'register_shop.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse("<b style='color:red;'>Username or Password is incorrect<b>")

        login(request, user)
        # Creating a Custom User.
        try:
            myUser = CustomUser.objects.get(user = user)
        except Exception as e:
            if user.is_superuser:
                # Register new Custom User for existing admin 
                newUser = CustomUser()
                newUser.user = user
                newUser.userType = "admin"
                newUser.save()
                return redirect("home")
            return HttpResponse("Something went wrong")

        return redirect("home")


    return render(request, 'loginUser.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

