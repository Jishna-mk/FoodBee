from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from catering.models import CateringProfile
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout




# Create your views here.

def admin_signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("viewCaterings")
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("admin_signin")

    return render(request,"admin/admin_signin.html")

def admin_signout(request):
    logout(request)
    return redirect("admin_signin")




def viewCaterings(request):
    catering = CateringProfile.objects.all().order_by("-id")
    # total_products = ProductList.objects.all().count()
    total_caterings = CateringProfile.objects.all().count()
    # total_bookings = Booking.objects.all().count()
    return render(request,"admin/view-caterings.html",{"caterings":catering,"total_caterings":total_caterings})




def approveCatering(request,m_id):
    catering = User.objects.get(id = m_id)
    catering.is_active = True
    catering.save()
    messages.success(request,"Approved as Catering")
    return redirect("viewCaterings")


from django.shortcuts import get_object_or_404
from django.contrib import messages




def removeCatering(request, m_id):
    try:
        catering = get_object_or_404(User, id=m_id)

        # Access related profile using the default related name (user_set)
        catering_profile_set = catering.cateringprofile_set.all()

        # Assuming there is only one related profile, you can delete it
        if catering_profile_set:
            catering_profile_set[0].delete()

        # Delete the User instance
        catering.delete()

        messages.success(request, "Removed Catering")
    except Exception as e:
        # Print the exception for debugging
        print(f"Error removing catering: {str(e)}")
        messages.error(request, "Error removing catering")

    return redirect("viewCaterings")