from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse, Http404
from dictionary2.topics.models import Entry, Topic, Category, Favorite
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def topicView(request, slug, id):

    try:
        topics = Topic.objects.get(slug=slug)
        context = {
            'topics': topics,
        }
        total = Favorite.objects.filter(entry=id).count()
        contact_list = Entry.objects.selected_related("topic").filtew(baslik_id=id)
        paginator = Paginator(contact_list, 5)
    except Topic.DoesNotExist:
        context = {
            'topics': None,
        }



    return render(request, 'topics/title.html', context)

