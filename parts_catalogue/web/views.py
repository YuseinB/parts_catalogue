from django.shortcuts import render, redirect
from .forms import PartForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Part


def index(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'index.html', context)


class PartDetailView(View):
    template_name = 'part_detail.html'

    def get(self, request, pk):
        part = Part.objects.get(pk=pk)
        return render(request, self.template_name, {'part': part})


@login_required()
def add_part(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PartForm()
    return render(request, 'add_part.html', {'form': form})


@login_required()
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})
