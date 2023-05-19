from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(("Shahar/Tuman"), max_length=255)

    def __str__(self):
        return self.name

class OrganizationCategory(models.Model):
    name = models.CharField(("Tibbiy muassasa kategoriyasi"),max_length=250)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(("Tibbiy muassasa nomi"), max_length=255)
    description = models.TextField(("Tavsif"),blank=True, null=True)
    image = models.ImageField(null=True)
    category = models.ForeignKey(OrganizationCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    working_time = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longtitude = models.TextField(blank=True, null=True)
    phone_numbers = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name

    # def location(self):
    #     return (self.latitude, self.longtitude)


class OrganizationImage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    path = models.ImageField(null=True)
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class OrganizationFeedback(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class SpecialistCategory(models.Model):
    name = models.CharField(("Mutaxasisligi"), max_length=255)

    def __str__(self):
        return self.name


class Specialist(models.Model):
    full_name = models.CharField(("Mutaxasis Ism sharifi"), max_length=255)
    photo = models.ImageField(null=True)
    category = models.ForeignKey(SpecialistCategory, on_delete=models.CASCADE, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class ServiceCategory(models.Model):
    name = models.CharField(("Tibbiy xizmat kategoriyasi"),max_length=255)
    alias = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(("Tibbiy xizmat nomi"),max_length=255)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    alias = models.TextField(blank=True, null=True)
    excerpt = models.TextField()
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ServiceImage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    path = models.ImageField(null=True)
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class OrganizationService(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.service.name








