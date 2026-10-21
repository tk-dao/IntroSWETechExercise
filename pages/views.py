from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q

from .forms import PartForm
from .models import Part

def hello_world(request):
    return HttpResponse("Hello World!")

def part_list(request):
    query = request.GET.get("q", "")
    category = request.GET.get("category", "")
    
    parts = Part.objects.order_by("-created_at")
    
    if query:
        parts = parts.filter(
            Q(name__icontains=query)
            | Q(brand__icontains=query)
            | Q(build__icontains=query)
            | Q(notes__icontains=query)
        )
    if category:
        parts = parts.filter(category=category)
        
    return render(request, "pages/part_list.html", {
        "parts": parts,
        "query": query,
        "category": category,
        "categories": Part.CATEGORY_CHOICES
    })

def add_part(request):
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("part_list")
    else:
        form = PartForm()
        
    return render(request, "pages/add_part.html", {"form": form})

    
    
