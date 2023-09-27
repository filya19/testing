from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('kraty/', views.kraty, name='kraty'),
    path('kraty/<slug:kraty_slug>', views.kraty_detail, name='kraty_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # for media resources
