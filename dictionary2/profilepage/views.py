from django.shortcuts import render
from dictionary2.topics.models import Entry, Topic, Category, Favorite
from django.db.models import Count

def profile_page(request):
    try:
        populer = Topic.objects.annotate(entry_count=Count('entry')).order_by('-entry_count')
        context = {
            'populer': populer,
        }
    except:
        return render(request, 'base/home.html')

    return render(request, 'pages/profil.html')


def ayarlar(request):
    try:
        populer = Topic.objects.annotate(entry_count=Count('entry')).order_by('-entry_count')
        context = {
            'populer': populer,
        }
    except:
        return render(request, 'base/home.html')

    return render(request, 'pages/ayarlar.html', context)

def mesajlar(request):
    try:
        today = Topic.topic_today.all()
        context = {
            'today': today,
        }
    except Topic.DoesNotExist:
        context = {
            'today': None,
        }

    return render(request, 'pages/mesajlar.html', context)



