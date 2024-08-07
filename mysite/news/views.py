from django.shortcuts import render, get_object_or_404

from .models import News, Category


def get_index(request):
    news = News.objects.order_by('-created_at')

    context = {'news': news,
               'title': 'Список новостей'}
    return render(request,
                  'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(id=category_id)

    return render(request,
                  'news/category.html',
                  {'news': news})


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request,
                  'news/view_news.html',
                  {'news_item': news_item})  
