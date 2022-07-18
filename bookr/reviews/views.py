from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "mundo"
    return render(request, "base.html",{"name":name})

def searchView(request):
    searchQuery = request.GET.get("search") or "Nada"
    return render(request, "searchResult.html",{"searchQuery":searchQuery})