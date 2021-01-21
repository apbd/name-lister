from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .forms import PersonForm

# Create your views here.
from .models import Person

import json
from pprint import pprint


def names_view(request):
    name_list = Person.objects.all()

    context = {
        'name_list': name_list,
    }

    return render(request, 'names/names.html', context)


def upload_view(request):
    """
    if request.method == 'POST':
        json_file_form = UploadJsonFileForm(request.POST, request.FILES)
        print("S")

        if json_file_form.is_valid():
            # file is saved
            handle_uploaded_file(request.FILES['file'])
            json_file_form.save()
            messages.success(request, 'Name and amount added.')
    else:
        json_file_form = UploadJsonFileForm()
        """
    try:
        uploaded_file = None
        if request.method == 'GET':
            add_names_to_database(read_names_json())

        if request.method == 'POST':
            uploaded_file = request.FILES['json']
            if uploaded_file.content_type == "application/json":
                print(uploaded_file.name)
                print(uploaded_file.content_type)
                handle_uploaded_file(request.FILES['json'])
                read_names_json()
    except KeyError:
        print("Error handling the uploaded file. No file was given.")


    context = {
        'json_file_form': uploaded_file

    }
    return render(request, 'upload/upload.html', context)


def handle_uploaded_file(f):
    with open('names.json', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def read_names_json():
    with open('names.json', 'r') as f:
        data = json.load(f)     # loads

    pprint(data)
    return data


def add_names_to_database(data):
    #print(json)

    print(data["names"])
    print(data["names"][0])
    for person in data["names"]:
        print(not Person.objects.filter(name=person["name"], amount=person["amount"]).exists())
        if not Person.objects.filter(name=person["name"], amount=person["amount"]).exists():

            person_obj = Person(name=person["name"], amount=person["amount"])
            print(person_obj)
            person_obj.save()

        #print(person["name"])
        #person_obj.name = person["name"]
        #person_obj.amount = person["amount"]


    """
    for lists in data.items():
        for lst in lists:
            for person in lst:
                for name in person:
                    print(name)
    """

