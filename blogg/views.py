from django.shortcuts import render ,redirect , get_object_or_404  
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import Registrationform , Postform
from django.contrib import messages
# Create your views here.

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful! You can Login the BLogg")
            return redirect('login')
    else:
        form = Registrationform()
    return render(request,'registration/register.html',{'form': form})

# Create View
@login_required
def create_post(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            form.save()
            return redirect('Posts')
    else:
        form = Postform()
    return render(request,'create_post.html',{'form':form})

#Update view

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('Posts')  # or redirect to post_detail if preferred
    else:
        form = Postform(instance=post)

    return render(request, 'update_post.html', {'form': form})

#Delete Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed

@login_required
@csrf_exempt
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('Posts')

    return HttpResponseNotAllowed(['POST'])
