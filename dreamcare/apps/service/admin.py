from django.contrib import admin
from dreamcare.apps.service.models import ServiceCategory, ServiceSubCategory


admin.site.register([ServiceCategory, ServiceSubCategory])
