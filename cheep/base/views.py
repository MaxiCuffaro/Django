from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .models import *
# Create your views here.

from .models import Post, Comment

def loginPage(request):
    if (request.method =='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'se inicio sesion')
                return redirect('/')
        messages.error(request, 'ocurrio un error')
    
    return render (request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('/')

def home(request):
   posts = Post.objects.order_by('-created')
   return render (request, 'home.html', { 'posts' : posts })

def registerPage(request):
    if (request.method =='POST'):
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if (password != confirm_password):
            messages.error(request, 'contraseñas incorrectas')
            return redirect('/registro')
        User.objects.create_user(username, first_name=name, email=email, last_name=last_name, password=password)
        return redirect('/')
    return render(request, 'register.html')


def post(request, id = None):
    if request.method =='POST':
        id = request.POST.get('id')
        if (id is None):
            Post.objects.create(
                title = request.POST.get('title'),
                text = request.POST.get('text'),
                user = request.user
            )
            messages.success(request, 'Enviado con exito')
            return redirect('/')
        else: 
            p = Post.objects.get(id = id)
            if(p.user == request.user):
                p.title = request.POST.get('title')
                p.text = request.POST.get('text')
                p.save()

    context = {}
    if id is not None:
        p = Post.objects.get(id = id)
        context ['post'] = p
 
    return render (request, 'post.html', context)

def comment(request):
    p = Post.objects.get(id = request.POST.get('post'))
    Comment.objects.create(
        text = request.POST.get('text'),
        user = request.user,
        post = p
    )
    return redirect('/')

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'profile.html', {'user':user, 'posts':posts})

def feed(request):
    posts = Post.objects.all()
    context= {'posts': posts}
    return render(request, 'feed.html', context)

