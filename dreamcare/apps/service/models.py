from django.db import models
from dreamcare.apps.accounts.models import User


class ServiceCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    is_inactive = models.BooleanField(default=False, db_index=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return str(self.name)


class ServiceSubCategory(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    is_inactive = models.BooleanField(default=False, db_index=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return str(self.name)


class ProviderServices(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    service_subcategory = models.ForeignKey(ServiceSubCategory, on_delete=models.CASCADE)

