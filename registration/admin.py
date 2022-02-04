from django.contrib import admin
from .models import users,region, professions
#.django.contrib.auth.

# Register your models here.
class admincust(admin.ModelAdmin):
    list_display=['fname','lname','slug','phone_no','date', 'time']
    list_filter =['date']
    prepopulated_fields={'slug':('fname','lname')}

admin.site.register(users, admincust)
admin.site.register(region)
admin.site.register(professions)