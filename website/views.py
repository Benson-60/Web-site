from django.shortcuts import render


def index(request):
    return render(request,'websites/index.html')