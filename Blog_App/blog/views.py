from django.shortcuts import render


def landing(request):
    return render(request,"blog/index.html")

def blogs():
    pass
