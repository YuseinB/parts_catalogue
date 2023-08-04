from django.shortcuts import render
from parts_catalogue.web.models import Part


def search_parts(request):
    query = request.GET.get('q')
    if query:
        parts = Part.objects.filter(name__icontains=query)
    else:
        parts = Part.objects.all()
    return render(request, 'search_parts.html', {'parts': parts, 'query': query})
