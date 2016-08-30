# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Count
from dictionary2.topics.models import Entry, Topic, Category, Favorite


def entry_view(request):
    category = Category.objects.first()
    topics = Topic.objects.all().prefetch_related('entry_set')[6:11]
    populer = Topic.objects.annotate(entry_count=Count('entry')).order_by('-entry_count')
    context = {
        'topics': topics,
        'category': category,
        'populer': populer,
    }
    return render(request, 'topics/title.html', context)

def today(request):
    try:
        today = Topic.topic_today.all()
        context = {
            'today': today,
        }
    except Topic.DoesNotExist:
        context = {
            'today': None,
        }

    return render(request, 'topics/kanallar/bugun.html', context)

def populer(request):
    try:
        populer = Topic.objects.annotate(entry_count=Count('entry')).order_by('-entry_count')

        context = {
            'populer': populer,
        }
    except:
        return render(request, 'base2.html')

    return render(request, 'topics/kanallar/populer.html', context)


def by_category(request, category):

    category = get_object_or_404(Category, pk=category)

    topics = Topic.objects.filter(category=category).prefetch_related('entry_set')

    return render(request, 'topics/kanallar/by_category.html')

def basiboslar(request, category):
    category = get_object_or_404(Category, pk=category)

    topics = Topic.objects.filter(category=None).prefetch_related('entry_set')

    return render(request, 'topics/kanallar/basiboslar.html')


def favorite(request):
    pass
#http://www.tangowithdjango.com/book/chapters/ajax.html




