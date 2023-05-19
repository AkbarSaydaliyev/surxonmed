# import json
from django.forms.models import model_to_dict
from algoliasearch.search_client import SearchClient
from django.core import serializers
from algoliasearch_django import AlgoliaIndex   
from algoliasearch_django.decorators import register

from .models import (
    Organization,
    Specialist,
    OrganizationService
)

client = SearchClient.create('L0AL6B1MBP', 'ef02206be1fadf824eee9f8c9e6fb4ca')

@register(Organization)
class OrganizationIndex(AlgoliaIndex):
    fields = ('name', 'category', 'image', 'location', 'working_time', 'address', 'latitude', 'longtitude', 'phone_numbers' )
    geo_field = 'location'
    settings = {'searchableAttributes': ['name', 'category']}
    index_name = 'organization_index'


organization_index = client.init_index('organization_index')
organizations = Organization.objects.all()
organization_data = []
for organization in organizations:
    organization_objects = {
        "objectID": organization.id,
        "name": organization.name,
        "description": organization.description,
        "image": organization.image.url,
        "category": organization.category,
        "location": organization.location,
        "working_time": organization.working_time,
        "address": organization.address,
        "latitude": organization.latitude,
        "longtitude": organization.longtitude,
        "phone_numbers": organization.phone_numbers,
    }
    organization_data.append(organization_objects)

organization_index.save_objects(organization_data)

@register(Specialist)
class SpecialistIndex(AlgoliaIndex):
    fields = ('full_name', 'photo', 'category', 'organization', 'description')
    settings = {'searchableAttributes': ['full_name', 'category']}
    index_name = 'specialist_index'


specialist_index = client.init_index('specialist_index')

specialists = Specialist.objects.all()
specialists_data = []
for spec in specialists:
    specialist_objects = {
        "objectID": spec.pk,
        "full_name": spec.full_name,
        "photo": spec.photo.url,
        "category": spec.category.name,
        "organization": {
            "objectID": spec.organization.pk,
            "name": spec.organization,
            "address": spec.organization.address,
            "latitude": spec.organization.latitude,
            "longtitude": spec.organization.longtitude,
            "description": spec.organization.description,
            "image": spec.organization.image.url,
            "category": spec.organization.category,
            "location": spec.organization.location,
            "working_time": spec.organization.working_time,
            "address": spec.organization.address,
            "latitude": spec.organization.latitude,
            "longtitude": spec.organization.longtitude,
            "phone_numbers": spec.organization.phone_numbers, 
        },
        "description": spec.description,
    }
    specialists_data.append(specialist_objects)

specialist_index.save_objects(specialists_data)




@register(OrganizationService)
class OrganizationServiceIndex(AlgoliaIndex):
    fields = ('organization', 'service', 'price')
    settings = {'searchableAttributes': ['organization', 'service']}
    index_name = 'organization_service_index'


organization_service_index = client.init_index('organization_service_index')

organization_services = OrganizationService.objects.all()
organization_services_data = []
for org_service in organization_services:
    organization_service_objects = {
        "objectID": org_service.pk,
        "service": org_service.service,
        "organization": {
            "objectID": org_service.organization.pk,
            "name": org_service.organization,
            "address": org_service.organization.address,
            "latitude": org_service.organization.latitude,
            "longtitude": org_service.organization.longtitude,
            "description": org_service.organization.description,
            "image": org_service.organization.image.url,
            "category": org_service.organization.category,
            "location": org_service.organization.location,
            "working_time": org_service.organization.working_time,
            "address": org_service.organization.address,
            "latitude": org_service.organization.latitude,
            "longtitude": org_service.organization.longtitude,
            "phone_numbers": org_service.organization.phone_numbers,
        },
        "description": org_service.service.excerpt,
        "service_alias": org_service.service.alias,
        "price": org_service.price,
    }
    organization_services_data.append(organization_service_objects)

organization_service_index.save_objects(organization_services_data)


