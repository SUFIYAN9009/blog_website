from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import TravelPost, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# ---------------- HOME ----------------
def home(request):
    category = request.GET.get('category')

    if category:
        posts = TravelPost.objects.filter(category=category).order_by('-created_at')
    else:
        posts = TravelPost.objects.all().order_by('-created_at')

    return render(request, 'home.html', {'posts': posts})


# -------- HEADER FOOTER PAGE --------
def header_footer(request):
    return render(request, 'header_footer.html')


# ---------------- STORIES ----------------
def stories(request):
    posts = TravelPost.objects.all()
    return render(request, 'stories.html', {'posts': posts})


# ---------------- GUIDES ----------------
def guides(request):
    return render(request, 'guides.html')


# ---------------- CART / DETAIL PAGE ----------------
def cart_image(request, id):
    post = get_object_or_404(TravelPost, id=id)
    return render(request, 'cart.html', {'post': post})


# ---------------- SIGNUP ----------------
def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')   # ✅ go to login page

    return render(request, 'signup.html', {'form': form})



# DASHBOARD

@login_required
def dashboard(request):
    posts = TravelPost.objects.filter(user=request.user)[:3]
    return render(request, 'dashboard.html', {'posts': posts})


# CREATE POST
@login_required
def create_post(request):

    if request.method == "POST":

        TravelPost.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            picture=request.FILES.get('picture')   # IMPORTANT FIX
        )

        return redirect('home')

    return render(request, 'create_post.html')



@login_required
def add_comment(request, id):
    post = get_object_or_404(TravelPost, id=id)

    if request.method == "POST":
        text = request.POST.get('text')

        if text:
            Comment.objects.create(
                user=request.user,
                post=post,
                text=text
            )

    return redirect('cart1', id=post.id)   # back to post page


@login_required
def like_post(request, id):
    post = get_object_or_404(TravelPost, id=id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('cart1', id=post.id)

def about(request):
    return render(request, 'about.html')