from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserAddForm
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login
from catering.models import FoodItem
from catering.models import CateringProfile
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,"index.html")

def food_list(request):
    food_items = FoodItem.objects.all()
    return render(request, 'user/viewpage.html', {'food_items': food_items})


def register(request):
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='users')
            user.groups.add(group)
            login(request, user)  # Correct usage of login function
            messages.success(request, "New User Created")
            return redirect('user_login')
        else:
            messages.error(request, "Form validation failed. Please try a different password.")
            print("Form errors:", form.errors)
    else:
        form = UserAddForm()
    return render(request,"user/register.html",{"form":form})

def user_login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("food_list")
        else:
            
            messages.info(request,"Username or Password Incorrect")
            return redirect("user_login")
    return render(request,"user/login.html")

def signout(request):
    
    logout(request)
    return redirect('user_login')


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('view_profile')  
    else:
        form = UserProfileForm()

    return render(request, 'user/create_profile.html', {'form': form})


@login_required
def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'user/view_profile.html', {'user_profile': user_profile})

def edit_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')  
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user/edit_profile.html', {'form': form})


