from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contact, Inquiry, Property
from django.contrib.auth.views import LoginView
from django.contrib import messages
import random
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')

def property_list(request):
    properties=Property.objects.all()
    property_type = request.GET.get("property_type")
    location = request.GET.get("location")
    budget = request.GET.get("budget")

    if property_type:
        properties = properties.filter(property_type=property_type)

    if location:
        properties = properties.filter(location=location)

    if budget:
        properties = properties.filter(price__lte=budget)

    return render(request,'property_list.html',{'properties':properties})

def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'property_detail.html', {'property': property})

@login_required
def contact_owner(request,id):
    property = get_object_or_404(Property, id=id)
    owner = property.owner 
    return render(request,'contact_owner.html',{'owner': property.owner})


def contact_us(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        messages.success(request, "Message sent successfully!")
        return redirect('contact') 
    return render(request, 'contact.html')

def inquiry(request):
    if request.method == 'POST':
        Inquiry.objects.create(
            property_type=request.POST['property_type'],
            location=request.POST['location'],
            budget=request.POST['budget'],
            phone=request.POST['phone'],
            email=request.POST['email']
        )
        
    return render(request, 'inquiry.html')

class CustomLoginView(LoginView):
    template_name = "login.html"
    
def book_property(request):
    return render(request,'book_property.html')

def book_property(request):
    booking_done = False

    if request.method == "POST":
        booking_done = True

    return render(request, "book_property.html", {
        "booking_done": booking_done
    })


def location(request):
    return render(request,'location.html')

def signup_view(request):
    if request.method == "POST":
        # create user here
        messages.success(request, "Account created successfully!")
        return redirect("signup")

    return render(request, "login.html")