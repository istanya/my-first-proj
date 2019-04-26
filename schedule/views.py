from django.shortcuts import render
from django.utils import timezone
from .models import Record

def post_list(request):
    records = Record.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'schedule/post_list.html', {'records': records})