from django.contrib import admin

# Register your models here.
from users import models

admin.site.register(models.Driverprofile)
admin.site.register(models.Userprofile)
