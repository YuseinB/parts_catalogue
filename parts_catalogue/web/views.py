from django.shortcuts import render, redirect, get_object_or_404
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


class Contacts(View):
    def get(self, request):
        return render(request, 'contacts.html')


class WhoAreWe(View):
    def get(self, request):
        return render(request, 'whe_are.html')


class PartDetailView(View):
    template_name = 'part_detail.html'

    def get(self, request, pk):
        part = Part.objects.get(pk=pk)
        return render(request, self.template_name, {'part': part})


@login_required
def add_part(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PartForm()
    return render(request, 'add_part.html', {'form': form})


@login_required
def edit_part(request, pk):
    part = get_object_or_404(Part, pk=pk)

    if request.method == 'POST':
        form = PartForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('part_detail', pk=pk)  # Променете 'part_detail' с името на вашия изглед за детайли на частта
    else:
        form = PartForm(instance=part)

    return render(request, 'edit_part.html', {'form': form})


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})
