from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Images
from django.http import JsonResponse
import boto3
import json
from django.middleware.csrf import get_token


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
    csrf_token = get_token(request)
    return render(request, 'images_app/pic.html', {'pic': pic, 'csrf_token': csrf_token})


def aws(request, id):
    pic = Images.objects.get(id = id)
    session = boto3.Session(region_name='us-west-2')
    rekognition = session.client('rekognition')

    # Cargar imagen
    with open('.' + pic.file.url, 'rb') as image_file:
        image = image_file.read()
    response = rekognition.detect_faces(Image = { 'Bytes': image }, Attributes = [ 'ALL' ])
    filtered_faces = filter(lambda face: face["AgeRange"]["Low"] >= 18, response['FaceDetails'])
    filtered_faces = list(map(lambda face: face['BoundingBox'], filtered_faces))
    return JsonResponse(filtered_faces, safe = False)
    
def delete(request):
    Images.objects.all().delete()
    return redirect('index')

def ajax(request):
    list = []
    list.append({'x': 1, 'y': 3})
    list.append({'x': 2, 'y': 4})
    return JsonResponse(list, safe = False)

def usa_ajax(request):
    return render(request, 'images_app/usa_ajax.html')


def blur(request, id):
    image = Images.objects.get(id = id)
    body = json.loads(request.body)
    coords = body.get('coords')
    print(coords)
