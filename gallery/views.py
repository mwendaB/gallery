from django.http  import HttpResponse
from django.shortcuts import redirect, render
from .models import Image, Category, Location

# Create your views here.
def index(request):
    images=Image.objects.all()
    locations = Location.all_locations()

    
    return render(request,'index.html',{'images': images, 'locations': locations})
    

def search_pictures(request):
    if request.method == "POST":
        search = request.POST['pictures']
        pictures = Image.search_by_category(search)
        print(pictures)
        
        return render(request,'search_pictures.html', {"pictures":pictures,"search":search})
    return render(request,'search_pictures.html')



    
def get_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_category = request.GET.get("category").lower()
        searched_category = Image.search_by_category(search_category)
        message = f"{search_category}"
        locations = Location.objects.all()

        return render(request, 'search.html', {"message": message, "images": searched_category, 'locations': locations})

    else:
        locations = Location.objects.all()
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message, 'locations': locations})


    
def location_kenya(request):
    images = Image.filter_by_location("Kenya")
    print(images)
    
    return render(request, 'location.html', {'images': images, })

def location_Europe(request):
    images = Image.filter_by_location("Europe")
    print(images)
    
    return render(request, 'location.html', {'images': images, })

