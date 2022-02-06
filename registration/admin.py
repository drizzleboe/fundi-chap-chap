from django.contrib import admin
from .models import user,region, profession
#.django.contrib.auth.

# Register your models here.
class admincust(admin.ModelAdmin):
    list_display=['fname','lname','phone_no','date', 'time']
    list_filter =['date']
    prepopulated_fields={'slug':('fname','lname')}

admin.site.register(user, admincust)
admin.site.register(region)
admin.site.register(profession)