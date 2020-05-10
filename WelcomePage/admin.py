from django.contrib import admin
from .models import students,UserProfiles

# Register your models here.
admin.site.register(students)
admin.site.register(UserProfiles)