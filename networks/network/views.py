from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

from .models import User, Post, Follow


def index(request):
    allposts = Post.objects.all().order_by("-id")
    # Pagination
    paginator = Paginator(allposts, 10)
    # get current page number
    page_number = request.GET.get("page")
    # get posts for current page number
    posts = paginator.get_page(page_number)
    
    return render(request, "network/index.html",{
        "posts": posts
    })

@login_required
def followingPost(request):
    user = request.user
    user_following = Follow.objects.filter(follower=user).values_list('following', flat=True)
    following_post = Post.objects.filter(author__in=user_following).order_by('-id')

    paginator = Paginator(following_post, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, "network/following.html", {
        "posts": posts
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
def newPost(request):
    if (request.method == "POST"):
        content = request.POST["content"]
        author = User.objects.get(pk=request.user.id)

        post = Post(content=content, author=author)
        post.save()

        return HttpResponseRedirect(reverse(index))


@login_required
def editPost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.user != post.author:
        return HttpResponseForbidden("You are not authroized to edit this post.")

    if request.method == "POST":
        new_content = request.POST.get("content", "").strip()

        if new_content:
            post.content = new_content
            post.isEdited = True
            post.save()
            return HttpResponseRedirect(reverse(index))

    return render(request, "network/editPost.html", {
        "post": post
    })

def profile(request, profile_id):
    is_following = False
    profileData = User.objects.get(pk=profile_id)
    allPostsData = Post.objects.filter(author=profileData).order_by("-id")
    
    # Pagination
    paginator = Paginator(allPostsData, 10)
    # get current page number
    page_number = request.GET.get("page")
    # get posts for current page number
    posts = paginator.get_page(page_number)

    if request.user.is_authenticated:
        follow_reln = Follow.objects.filter(follower=request.user, following=profileData)
        is_following = Follow.objects.filter(
            follower=request.user, 
            following=profileData
        ).exists()

    return render(request, "network/profile.html",{
        "posts": posts,
        "profile": profileData,
        "viewer_id": request.user.id if request.user.is_authenticated else None,
        "is_following": is_following
    })


@login_required
@require_POST
def followProfile(request, profile_id):
    follower = request.user
    following = get_object_or_404(User, pk=profile_id)

    if follower != following:
        follow_reln = Follow.objects.filter(follower=follower, following=following)

        if(follow_reln.exists()):
            follow_reln.delete()
            is_following = False
        else:
            Follow.objects.create(follower=follower, following=following)
            is_following = True

        follower_count = Follow.objects.filter(following=following).count()

        return JsonResponse({
            "is_following": is_following,
            "follower_count": follower_count
        })

    return JsonResponse({"error": "ERROR"}, status=400)


@login_required
@require_POST
def likePost(request, post_id):
    liked_by = request.user
    post_liked = get_object_or_404(Post, pk=post_id)

    if (liked_by in post_liked.likes.all()):
        post_liked.likes.remove(liked_by)
        is_liked = False
    else:
        post_liked.likes.add(liked_by)
        is_liked = True

    liked_count = post_liked.likes.count()
    return JsonResponse({
        "is_liked": is_liked,
        "liked_count": liked_count
    })