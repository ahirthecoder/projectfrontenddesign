from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "home.html")


# TODO Build This Page
def doc_view(request):
    return render(request, "home.html")