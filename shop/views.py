from django.shortcuts import render,get_object_or_404,redirect
from . import models,forms
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def homepage(request, category_slug=None):
    tovarlar = models.PC.objects.all()
    category = None
    categories = models.Category.objects.all()
    products = models.PC.objects.all()
    if category_slug:
        category = get_object_or_404(models.Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'home.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products,
                      'tovarlar':tovarlar
                  })


def product_detail(request,id):
    tovar = get_object_or_404(models.PC,id=id)
    comments = models.Comments.objects.filter(tovar=tovar)
    if request.method=='POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.tovar = tovar
            new_comment.username = request.user
            new_comment.save()
            return redirect('detail',id=tovar.id)
    else:
        comment_form = forms.CommentForm()
    return render(request,'detail.html',{
            'tovar':tovar,
            'comments':comments,
            'comment_form':comment_form
        })


def registration(request):
    if request.method =='POST':
        form  = forms.RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.RegForm()
    return render(request,'reg.html',{'form':form})

def signin(request):
    if request.method =='POST':
        form  = forms.LoginForm(request,data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form  = forms.LoginForm()
    return render(request,'login.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('home')
