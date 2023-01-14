from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Images


def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
             object = form.save()
        return redirect('display_pics')
        #return redirect('index', id=object.id)
    else:
        pictures = Images.objects.all()
        context = {
        'pictures': pictures
        }
        form = DocumentForm()
    return render(request, 'images_app/index.html', {'form': form, 'context': context})
    # return render(request, 'images_app/index.html', id=object.id {'form': form})



def pics(request):
    pictures = Images.objects.all()
    return render(request, 'images_app/display_pics.html', {'context': pictures})

def pic(request, id):
    pic = Images.objects.get(id = id)
    return render(request, 'images_app/pic.html', {'pic': pic})
    

def delete(request):
    Images.objects.all().delete()
    return redirect('index')