from django.shortcuts import render, redirect
from .forms import PartForm, CategoryForm


def index(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'index.html', context)


def add_part(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PartForm()
    return render(request, 'add_part.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})
