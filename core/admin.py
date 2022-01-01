from django.contrib import admin

from core.models import *

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Thing)
admin.site.register(Attraction)
admin.site.register(Tour)
admin.site.register(Picture)
admin.site.register(Plan)
admin.site.register(PlanThing)