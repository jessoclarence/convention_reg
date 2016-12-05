from django.conf import urls
from rest_framework import routers

from regmain import constants
from regmain import viewsets
from regmain import views


router = routers.DefaultRouter()

router.register(
    'families', viewsets.FamilyViewSet)
router.register(
    'churches', viewsets.ChurchViewSet)
router.register(
    'attendant_types',
    viewsets.AttendantTypeViewSet)
router.register(
    'contact_infos',
    viewsets.ContactInfoViewSet)
router.register(
    'airport_infos',
    viewsets.AirportInfoViewSet)
router.register(
    'transport', viewsets.TransportViewSet)
router.register(
    'special_requests',
    viewsets.SpecialRequestViewSet)
router.register(
    'person_infos',
    viewsets.PersonInfoViewSet)
router.register(
    'volunteer_types',
    viewsets.VolunteerTypeViewSet)
router.register(
    'events', viewsets.EventViewSet)
router.register(
    'regforms', viewsets.RegFormViewSet)
router.register(
    'person_volunteers',
    viewsets.PersonVolunteerViewSet)
router.register(
    'person_event_maps',
    viewsets.PersonEventMapViewSet)
router.register(
    'regform_person_maps',
    viewsets.RegFormPersonMapViewSet)


urlpatterns = [
    urls.url(r'^', urls.include(router.urls)),
    urls.url(
        r'^add_person/$', views.add_person,
        name='remgain_add_person'),
    urls.url(
        r'^add_contact_info/$', views.add_contact_info,
        name='remgain_add_contact_info'),
    urls.url(
        r'^add_family/$', views.add_family,
        name='remgain_add_family'),
    urls.url(
        r'^main_form/$', views.single_form,
        name='remain_single_form'),
]
