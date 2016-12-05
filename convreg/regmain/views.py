from django import shortcuts
from django import http
from django.views.decorators import csrf

import dateparser

from regmain import models


def single_form(request):
    context = {}
    if request.method == 'GET':
        return shortcuts.render(
            request, 'regmain/single_form.html', context)


@csrf.csrf_exempt
def add_family(request):
    context = {}

    if request.method == 'GET':
        return shortcuts.render(
            request, 'regmain/add_family.html', context)

    if request.method == 'POST':
        name = request.POST.get('name')

        family = models.Family(name=name)
        family.save()

        return http.JsonResponse(family.to_dict())


def add_contact_info(request):
    context = {}
    if request.method == 'GET':
        return shortcuts.render(
            request, 'regmain/add_contact_info.html', context)
    if request.method == 'POST':
        address = request.POST.get('address')
        cell_phone = request.POST.get('cell_phone')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')

        contact_info = models.ContactInfo(
            address=address,
            cell_phone=cell_phone,
            email=email,
            telephone=telephone)
        contact_info.save()
        return http.JsonResponse(contact_info.to_dict())


@csrf.csrf_exempt
def add_person(request):
    context = {}
    if request.method == 'GET':
        churches = models.Church.objects.all()
        context['churches'] = [c.to_dict() for c in churches]

        att_types = models.AttendantType.objects.all()
        context['att_types'] = [a.to_dict() for a in att_types]
        return shortcuts.render(
            request, 'regmain/add_person.html', context)

    if request.method == 'POST':
        return http.JsonResponse({'first_name': 'Jesso'})
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        sex = request.POST.get('sex')
        church_id = request.POST.get('church_id')
        family_id = request.POST.get('family_id')
        contact_info_id = request.POST.get('contact_info_id')
        att_type_id = request.POST.get('att_type_id')

        dob_obj = dateparser.parse(dob)
        church = models.Church.objects.get(id=church_id)
        family = models.Family.objects.get(id=family_id)
        contact_info = models.ContactInfo.objects.get(
            id=contact_info_id)
        att_type = models.AttendantType.objects.get(id=att_type_id)

        person = models.PersonInfo(
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            sex=sex,
            church=church,
            family=family,
            contact_info=contact_info,
            att_type=att_type)
        person.save()

        return http.JsonResponse(person.to_dict())
