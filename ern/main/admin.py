from django.contrib import admin
from .models import doctor,hospital,house,issue

admin.site.register(doctor)
admin.site.register(hospital)
admin.site.register(house)
admin.site.register(issue)
