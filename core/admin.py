from django.contrib import admin
from django.db import models
from .models import (
    Location, 
    OrganizationCategory, 
    Organization, 
    OrganizationFeedback, 
    OrganizationImage, 
    SpecialistCategory, 
    Specialist,
    ServiceCategory,
    Service,
    ServiceImage,
    OrganizationService,

)
# Register your models here.


admin.site.register(Location)
admin.site.register(OrganizationCategory)
admin.site.register(Organization)
admin.site.register(OrganizationFeedback)
admin.site.register(OrganizationImage)
admin.site.register(SpecialistCategory)
admin.site.register(Specialist)
admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(ServiceImage)
admin.site.register(OrganizationService)