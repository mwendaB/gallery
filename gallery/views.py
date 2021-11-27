from django.http  import HttpResponse
from .models import Image, Category, Location

# Create your views here.
def index(request):
    Image = Image.objects