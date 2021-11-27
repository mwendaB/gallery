from django.http  import HttpResponse
from django.shortcuts import render
from .models import Image, Category, Location

# Create your views here.
def index(request):
    images=Image.objects.all()
    locations = Location.all_locations()
    
    return render(request,'index.html',{'images': images, 'locations': locations})


def get_category(request):
    if 'Category' in request.GET and request.GET["category"]:
        search_category = request.GET.get("category").lower()
        searched_category = Image.filter_by_category(search_category)
        message = f"{search_category}"
        locations = Location.objects.all()

        return render(request, 'search.html', {"message": message, "images": searched_category, 'locations': locations})

    else:
        locations = Location.objects.all()
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message, 'locations': locations})


    
def location(request, location_id):
    locations = Location.objects.all()
    images = Image.objects.filter(location_id=location_id)
    location = Location.objects.get(id=location_id)
    title = location
    return render(request, 'location.html', {'images': images, 'locations': locations, 'title': title})

