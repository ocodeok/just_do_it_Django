from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm


class HomeView(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home News'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])

        return context


class ViewNews(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id' // Именованный параметр принимаемый в urlpatterns

