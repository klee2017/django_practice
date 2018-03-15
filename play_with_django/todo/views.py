from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 방법 1
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # 방법 2
            # post = Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
            # post.save()

            # 방법 3
            # post = Post.objects.create(title=form.cleaned_data['title'], content=form.cleaned_data['content'])

            # 방법 4
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/todo/')
    else:
        form = PostForm()
    return render(request, 'todo/post_form.html', {'form': form, })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/todo/')
    else:
        form = PostForm(instance=post)
    return render(request, 'todo/post_form.html', {'form': form, })

    pass
