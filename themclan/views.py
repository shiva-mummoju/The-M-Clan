from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'themclan/home.html', {'page_title': 'The M Clan'})

def projects(request):
    return render(request, 'themclan/projects.html', {'page_title': 'Projects'})

def threedayevent(request):
    return render(request, 'themclan/3DayEvent.html', {'page_title': '3 Day Event'})

def about(request):
    return render(request, 'themclan/about.html', {'page_title': 'About'})

def magazine(request):
    return render(request, 'themclan/magazine.html', {'page_title': 'Magazine'})

def pioneers(request):
    return render(request, 'themclan/pioneers.html', {'page_title': 'Pioneers'})

def hpvc(request):
    return render(request, 'themclan/hpvc.html', {'page_title': 'HPVC'})

def supra(request):
    return render(request, 'themclan/supra.html', {'page_title': 'SUPRA'})

def aero(request):
    return render(request, 'themclan/aero.html', {'page_title': 'AERO'})

def sdc(request):
    return render(request, 'themclan/sdc.html', {'page_title': 'SDC'})

def baja(request):
    return render(request, 'themclan/baja.html', {'page_title': 'BAJA'})

