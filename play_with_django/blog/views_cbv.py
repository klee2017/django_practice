from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().prefetch_related('tag_set', 'comment_set')
    paginate_by = 20


post_new = CreateView.as_view(model=Post)

post_list = PostListView.as_view()

post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))
