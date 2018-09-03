from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'themclan/home.html', {'page_title': 'The M Clan'})

def projects(request):
    return render(request, 'themclan/projects.html', {'page_title': 'The M Clan'})

def threedayevent(request):
    return render(request, 'themclan/3DayEvent.html', {'page_title': 'The M Clan'})

def about(request):
    return render(request, 'themclan/about.html', {'page_title': 'The M Clan'})

def magazine(request):
    return render(request, 'themclan/magazine.html', {'page_title': 'The M Clan'})

def pioneers(request):
    return render(request, 'themclan/pioneers.html', {'page_title': 'The M Clan'})

