from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('search/',views.get_category,name='category'),
    path('search_pictures/',views.search_pictures,name='search_pictures'),
    path('location_kenya/',views.location_kenya,name ='location_kenya'),
    path('location_Europe/',views.location_Europe,name ='location_Europe'),
    path('location_Asia/',views.location_Asia,name ='location_Asia'),
    path('location_Austraria/',views.location_Austraria,name ='location_Austraria'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)