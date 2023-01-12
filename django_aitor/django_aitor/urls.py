"""django_aitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from images_app import views
# added by me
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('pics', views.pics, name='pics')
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('pics/', views.pics, name='display_pics'),
    path('pic/<int:id>', views.pic, name='pic'),
    path('delete', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

