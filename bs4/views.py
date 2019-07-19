from django.shortcuts import render


# Create your views here.
def index1(request):
    return render(request, "bs4/index1.html")


def aboutus(request):
    return render(request, "bs4/aboutus.html")

def contactus(request):
    return render(request, "bs4/contactus.html")
