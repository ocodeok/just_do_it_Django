from django.http import HttpResponse
from django.shortcuts import render

from .models import News, Category


def get_index(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()

    context = {'news': news,
               'title': 'Список новостей',
               'categories': categories}
    return render(request,
                  'news/index.html', context)


def get_category(request, category_id):
    print('PRINT!', category_id)
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)

    return render(request,
                  'news/category.html',
                  {'news': news, 'categories': categories, 'category': category})