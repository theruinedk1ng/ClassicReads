from django.shortcuts import render, redirect
import random
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .models import BooksAndReviews
from django.contrib.auth.decorators import login_required


from .forms import CreateUserForm
from .models import *


quote_options = ['“And so it goes...” - Kurt Vonnegut', 
                    '“O teach me how I should forget to think” - William Shakespeare',
                    '“Nothing contributes so much to tranquilize the mind as a steady purpose” - Mary Shelley',
                    '“There is nothing alive more agonized than man / of all that breathe and crawl across the earth.” - Homer',
                    '“A thing is not necessarily true because a man dies for it.” - Oscar Wilde',
                    '“I don`t want to die without any scars” -  Chuck Palahniuk',
                    ]



def quotes(request):
    
    random_text = random.choice(quote_options)
    
    return render(request, 'books/main.html', {'random_text': random_text})

def homepage(request):
    
    random_text = random.choice(quote_options)
    
    return render(request, 'books/homepage.html', {'random_text': random_text})


def discover(request):
    
    return render(request, 'books/discover.html')

@login_required
def mybooks(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')

        if title and author:
            book = BooksAndReviews.objects.create(title=title, author=author)

        return redirect('mybooks') 

    query = request.GET.get('q')
    books = BooksAndReviews.objects.all().order_by('-date')
    if query:
        books = books.filter(title__icontains=query)

    return render(request, 'books/mybooks.html', {'books': books})


def signup_view(request):
    if request.method == 'POST':
        signup_form = CreateUserForm(request.POST)

        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('dashboard')  
    else:
        signup_form = CreateUserForm()

    return render(request, 'books/signuppage.html', {'signup_form': signup_form})

def handle_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            if request.POST.get('remember_me'):
                request.session.set_expiry(1209600) 
            else:
                request.session.set_expiry(0) 

            return redirect('dashboard')
    else:
        login_form = AuthenticationForm()

    return render(request, 'books/myprofile.html', {'login_form': login_form})

def logout(request):
    django_logout(request)
    return redirect('myprofile')

def myprofile(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            return redirect('signuppage')
        elif 'login' in request.POST:
            return handle_login(request)

    signup_form = CreateUserForm()
    login_form = AuthenticationForm()

    return render(request, 'books/myprofile.html', {'signup_form': signup_form, 'login_form': login_form})


def aboutus(request):
    return render(request, 'books/aboutus.html')

def success_page(request):
    return render(request, 'books/success.html')

def dashboard(request):

    return render(request, 'books/success.html')

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'books/success.html', context)


