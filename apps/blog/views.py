from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post



class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context