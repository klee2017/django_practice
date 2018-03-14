from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post


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
            post = Post.objects.create(**form.cleaned_data)
            return redirect('/todo/')
    else:
        form = PostForm()
    return render(request, 'todo/post_form.html', {'form': form, })
