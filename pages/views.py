from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PartForm
from .models import Part

def hello_world(request):
    return HttpResponse("Hello World!")

def part_list(request):
    parts = Part.objects.order_by("-created_at")
    return render(request, "pages/part_list.html", {"parts": parts})

def add_part(request):
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("part_list")
    else:
        form = PartForm()
        
    return render(request, "pages/add_part.html", {"form": form})

    
    
