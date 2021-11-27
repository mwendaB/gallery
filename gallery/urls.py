from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('',views.index,name='galleryHome'),
    url('search/',views.get_category,name='category'),
    url('location/<str:search_location>/',views.get_location,name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)