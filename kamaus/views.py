from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
from .models import SignUp, LoginAction, Contact
from .forms import CreateUserForm

def about(request):
    return render(request, 'about.html')
def index(request):
    return render(request, 'index.html')
def inquiries(request):
    return render(request, 'inquiries.html')

# Home view
def home(request):
    return render(request, 'home.html')

# Contact view
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save contact form submission
        Contact.objects.create(name=name, email=email, message=message)
        return render(request, 'contact.html', {'success': 'Your message has been sent!'})

    return render(request, 'contact.html')

# Sign-up view
def signup_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Save sign-up information in SignUp model
            SignUp.objects.create(user=user)

            return redirect('login_view')

    context = {'form': form}
    return render(request, "signup.html", context)

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            # Save login information in LoginAction model
            LoginAction.objects.create(user=user, login_date=timezone.now())

            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

