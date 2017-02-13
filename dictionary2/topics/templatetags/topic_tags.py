# -*- coding: utf-8 -*-

from django import template

from dictionary2.topics.models import Category
register = template.Library()

@register.assignment_tag
def get_categories():
    # kategorileri burada çağırıyoruz.

    category_list = Category.objects.all()
    return category_list

