from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document


def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'images_app/index.html', {'form': form})

def pics(request):
    pictures = Document.objects.all()
    context = {
        'pictures': pictures
    }
    return render(request, 'images_app/display_pics.html', context)
