from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "firstapp/index.html")

def page_1(request):
    return render(request, "firstapp/page_1.html")

def page_2(request):
    return render(request, "firstapp/page_2.html")