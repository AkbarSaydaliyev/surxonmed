from pprint import pprint
from django.shortcuts import render
from algoliasearch.search_client import SearchClient
from algoliasearch_django import raw_search
from django.http import HttpResponse
from django.views import generic, View
from .models import Organization, OrganizationCategory, OrganizationImage, Specialist, SpecialistCategory, Service, OrganizationService, OrganizationFeedback, OrganizationCategory, ServiceCategory
# from .index import OrganizationIndex

# Create your views here.

# client = SearchClient.create('L0AL6B1MBP', 'ef02206be1fadf824eee9f8c9e6fb4ca')


def index(request):
    organizationImage = OrganizationImage.objects.first()
    doctors = Specialist.objects.all()
    hospitals = Organization.objects.all()
    context = {
        'doctors': doctors,
        'hospitals': hospitals,
        'organizationImage': organizationImage
    }
    return render(request, 'base/index.html', context)

def search(request):
    query = request.GET.get('search')
    params = { "hitsPerPage": 5 }
    context = {}
    organizations_response = raw_search(Organization, query, params)
    specialists_response = raw_search(Specialist, query, params)
    services_response = raw_search(OrganizationService, query, params)
    if not organizations_response['nbHits'] and not specialists_response['nbHits'] and not services_response['nbHits']:
        context['errors'] = "So'rovingiz boyicha hech narsa topilmadi"
    else:
        organizations = {}
        if organizations_response['nbHits']:
            for organization in organizations_response['hits']:
                organizations[str(organization['objectID'])] = organization        
        if specialists_response['nbHits']:
            for doctor in specialists_response['hits']:
                if not doctor['organization']['objectID'] in organizations:
                    organizations[str(doctor['organization']['objectID'])] = doctor['organization'] 
                if not 'doctors' in organizations[str(doctor['organization']['objectID'])]:
                    organizations[str(doctor['organization']['objectID'])]['doctors'] = []    
                
                organizations[str(doctor['organization']['objectID'])]['doctors'].append(doctor)

        if services_response['nbHits']:
            for service in services_response['hits']:
                if not service['organization']['objectID'] in organizations:
                    organizations[str(service['organization']['objectID'])] = service['organization']
                if not 'services' in organizations[str(service['organization']['objectID'])]:
                    organizations[str(service['organization']['objectID'])]['services'] = []
                organizations[str(service['organization']['objectID'])]['services'].append(service)

        context['organizations'] = organizations
        locations = []
        for organization in organizations.values():
            locations.append({
                'label': organization['name'],
                'lat': organization['latitude'],
                'lng': organization['longtitude']
            })
        context['locations'] = locations
    return render(request, 'surxonmed/search_result.html', context)



def organizationDetail(request, pk):
    organization = Organization.objects.get(pk=pk)
    organization_services = organization.organizationservice_set.all()
    organization_doctors = organization.specialist_set.all()
    organization_feedbacks = organization.organizationfeedback_set.all()
    organization_images = organization.organizationimage_set.all()
    # for doctor in organization_doctors:
        
    context = {
        "organization": organization,
        "organization_services": organization_services,
        "organization_doctors": organization_doctors,
        "organization_feedbacks": organization_feedbacks,
        "organization_images": organization_images
    }
    locations = []
    locations.append({
        'label': organization.name,
        'lat': organization.latitude,
        'lng': organization.longtitude
    })
    context['locations'] = locations

    return render(request, 'surxonmed/organization_detail.html', context)

def doctorDetail(request, pk):
    doctor = Specialist.objects.get(pk=pk)
    context = {
        'doctor': doctor
    }
    return render(request, 'surxonmed/doctor_detail.html', context)

def doctors(request):
    doctors = Specialist.objects.all()
    categories = SpecialistCategory.objects.all()
    context = {
        'doctors': doctors,
        'categories': categories,
        # 'doctor_categories': doctor_categories
    }
    return render(request, 'surxonmed/doctors.html', context)

def hospitals(request):
    hospitals = Organization.objects.all()
    hospital_categories = OrganizationCategory.objects.all()
   
    context = {
        "hospitals": hospitals,
        'hospital_categories': hospital_categories,
    }
    return render(request, 'surxonmed/hospitals.html', context)

def services(request):
    services = OrganizationService.objects.all()
    service_category = ServiceCategory.objects.all()
    context = {
        'services': services,
        'service_category': service_category
    }
    return render(request, 'surxonmed/services.html', context)

def serviceDetail(request, pk):
    service = Service.objects.get(pk=pk)
    context = {
        'service': service
    }
    return render(request, 'surxonmed/service_detail.html', context)



def medicines(request):
    return render(request, 'surxonmed/medicines.html')

def posts(request):
    return render(request, 'surxonmed/posts.html')

def contact(request):
    return render(request, 'surxonmed/contact.html')