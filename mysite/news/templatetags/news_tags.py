from django import template
from django.db.models import Count, Q

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    categories = Category.objects.all()
    return categories


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = (Category.objects
                  .annotate(cnt=Count('news'))
                  .filter(cnt__gt=0))
    print('\n\n', categories, '\n\n')
    return {
        'categories': categories}
