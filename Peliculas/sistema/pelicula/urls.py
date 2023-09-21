from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('nosotros/', views.nosotros, name='nosotros'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)