from django.shortcuts import render

def profile(request):
    return render(request, 'materialize/users/profile.html')


def ayarlar(request):
    return render(request, 'pages/ayarlar.html')


def messages(request):
    return render(request, 'materialize/users/message.html')


def events(request):
    return render(request, 'materialize/users/event.html')




