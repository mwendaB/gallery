from django.contrib import admin
from .models import Location, Category, Image
# Register your models here.
from .models import Location, Category, Image
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('Category',)

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)