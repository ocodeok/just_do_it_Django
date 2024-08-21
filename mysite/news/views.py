from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

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
# def get_index(request):
#     news = News.objects.order_by('-created_at')
#
#     context = {'news': news,
#                'title': 'Список новостей'}
#     return render(request,
#                   'news/index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(id=category_id)
#
#     return render(request,
#                   'news/category.html',
#                   {'news': news})


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request,
                  'news/view_news.html',
                  {'news_item': news_item})


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)

    else:
        form = NewsForm()

    return render(request,
                  'news/add_news.html',
                  {"form": form})
