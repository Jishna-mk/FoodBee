from django.shortcuts import render,redirect
from .forms import FoodItemForm
from .models import FoodItem,CateringProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def food_view(request):
    food_items = FoodItem.objects.all()
    return render(request, 'catering/view_food.html', {'food_items': food_items})
   

from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.shortcuts import render, redirect
from users.forms import UserAddForm
from catering.forms import CateringProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



def cateringsignup(request):
    form=UserAddForm()
    catering_form = CateringProfileForm()
    if request.method=="POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Already Exists")
                return redirect('cateringsignup')
            if User.objects.filter(email=email).exists():
                messages.info(request,"This Emailid is Already Taken")
                return redirect('cateringsignup')
            
            new_user = form.save()
            new_user.is_active = False
            new_user.save()
                
            group = Group.objects.get(name='catering')
            new_user.groups.add(group) 

            catering_form = CateringProfileForm(request.POST,request.FILES)
            if catering_form.is_valid():
                catering = catering_form.save()
                catering.user = new_user
                catering.save()
                messages.success(request,"Registered as Catering! Wait for Approval")
                return redirect('cateringsignin')
            else:
                messages.success(request,"Couldn't perform  Signup")
                print(form.errors)

        else:
            messages.error(request,"Error in catering profile details.")
    return render(request,"catering/signup.html",{"form":form,"catering_form":catering_form})


def cateringsignin(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            messages.info(request,'Logged In Successfully')
            login(request, user1)
            group = request.user.groups.all()[0].name
            if(group == "catering"):
                return redirect('food_view')
            else:
                messages.info(request,'Username or Password Incorrect')
                return redirect("cateringsignout")
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('cateringsignin')
    return render(request,"catering/signin.html")

def cateringsignout(request):
    logout(request)
    return redirect('index')

@login_required
def add_food(request):
    try:
        catering_profile = CateringProfile.objects.get(user=request.user)
        catering_name = catering_profile.Catering_Name
    except CateringProfile.DoesNotExist:
        catering_name = None

    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.catering_name = catering_name
            food_item.save()
            return redirect('food_view')
    else:
        form = FoodItemForm()

    return render(request, 'catering/add_food.html', {'form': form})
def edit_food(request, food_id):
    food_item = get_object_or_404(FoodItem, pk=food_id)
    
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('food_view')
    else:
        form = FoodItemForm(instance=food_item)
    
    return render(request, 'catering/edit_food.html', {'form': form, 'food_item': food_item})



def delete_food(request,pk):
    food = FoodItem.objects.get(food_id=pk) 
    food.delete()
    messages.info(request,"item deleted")
    return redirect("food_view")
def book_item(request, food_id):
    food_item = get_object_or_404(FoodItem, pk=food_id)
    
    # Check if user has a profile
    if not hasattr(request.user, 'profile'):
        # Redirect to create profile page
        return redirect('create_profile')

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        if food_item.book_item(quantity, request.user):
            # Booking successful, you can proceed with your logic here
            return render(request, 'user/booking_success.html', {'food_item': food_item, 'quantity': quantity})
        else:
            # Quantity not available, handle accordingly (e.g., show an error message)
            return render(request, 'user/booking_error.html', {'food_item': food_item})

    return render(request, 'user/book_food.html', {'food_item': food_item})