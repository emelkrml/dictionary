# -*- coding: utf-8 -*-

import json

from idlelib.configDialog import is_int

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Count

from dictionary2.topics.models import Entry, Topic, Category, Favorite


# def entry_view(request):
#     category = Category.objects.first()
#     topics = Topic.objects.all().prefetch_related('entry_set')[10:]
#     populer = Topic.objects.annotate(entry_count=Count('entry')).order_by('-entry_count')
#     context = {
#         'topics': topics,
#         'category': category,
#         'populer': populer,
#     }
#     return render(request, 'topics/home.html', context)

def home(request):

    popular = Topic.objects.all().annotate(entry_count=Count('entry')).order_by('-entry_count')
    context = {"popular": popular}

    return render(request, 'base/home.html', context)


def get_today(request):

    topics = Topic.topic_today.all().values('id', 'title').prefetch_related('entry_set')

    return HttpResponse(json.dumps(list(topics)), content_type="application/json")


def get_popular(request):

    topics = Topic.objects.all().annotate(entry_count=Count('entry')).values('id', 'title').order_by('entry_count')

    return HttpResponse(json.dumps(list(topics)), content_type="application/json")


def get_junior_user(request):

    topics = Topic.objects.all().filter(user__junior=1).values('id', 'title')

    return HttpResponse(json.dumps(list(topics)), content_type="application/json")


def get_stray(request):

    topics = Topic.objects.all().filter(category=None).only('entry_set')

    return HttpResponse(json.dumps(list(topics)), content_type="application/json")


def by_category(request):

    # bugün, populer, çaylaklar ve badi dışındaki diğer kategoriler
    # burada çağırılır.

    category_id = request.POST.get('category_id', None)

    topics = Topic.objects.filter(category__id=category_id).values('id', 'title').prefetch_related('-entry_set')

    return HttpResponse(json.dumps(list(topics)), content_type="application/json")






# def entry(request):
#     populer = Topic.objects.annotate(entry_count=Count('entry')).order_by('-entry_count')
#     topics = Topic.objects.get(entry__content='entry')
#     context = {
#         'populer': populer,
#         'topics': topics,
#     }
#     return render(request, 'topics/entry.html', context)
#
#
# def today(request):
#     try:
#         today = Topic.topic_today.all()
#         context = {
#             'today': today,
#         }
#     except Topic.DoesNotExist:
#         context = {
#             'today': None,
#         }
#
#     return render(request, 'topics/bugun.html', context)
#
#
# def populer(request):
#     try:
#         populer = Topic.objects.annotate(entry_count=Count('entry')).order_by('-entry_count')
#
#         context = {
#             'populer': populer,
#         }
#     except:
#         return render(request, 'topics/home.html')
#
#     return render(request, 'topics/populer.html', context)
#
#
# def caylak(request):
#     try:
#         caylak = Topic.objects.filter(user__junior=1)
#         context = {
#             'caylak': caylak,
#         }
#     except:
#         return render(request, 'base/home.html')
#
#     return render(request, 'topics/caylaklar.html', context)
#
#
# def basiboslar(request):
#     topics = Topic.objects.filter(category=None).prefetch_related('entry_set')
#     context = {
#         'topics': topics,
#     }
#
#     return render(request, 'topics/basiboslar.html', context)


'''
def favorite(request):
    context = RequestContext(request)
    entry_id = None
    if request.method == 'GET':
        e_id = request.GET['entry_id']

    fav = 0
    if e_id:
        entry = Entry.objects.get(id=int(e_id))
        if entry:
            fav = entry.fav + 1
            entry.fav = fav
            entry.save()

    return HttpResponse(fav)
'''




