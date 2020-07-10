from django.shortcuts import render, redirect
from .models import Message
from .form import MessageModelForm


def page_not_found(request, exception):
    """404 page"""
    return render(request, '404.html', status=404)


def page_error(request):
    """500 page"""
    return render(request, '500.html', status=500)


def index(request):
    messages = Message.objects.all().order_by('-id')
    if request.method == 'POST':
        form = MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'index.html', locals())
