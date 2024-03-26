from django.shortcuts import get_object_or_404, render
from flask import redirect
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts':posts})

def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        post.title = title
        post.body = body
        post.save()
    return render(request, 'edit.html',{'post':post})