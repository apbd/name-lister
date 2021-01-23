from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .forms import PersonForm

# Create your views here.
from .models import Person

import json
from pprint import pprint


def names_view(request, *args, **kwargs):
    name_list = Person.objects.all()

    # what table order is needed
    if request.GET.get('sortamount') == "Sort by amount":
        name_list = Person.objects.order_by('-amount')[0:]
    elif request.GET.get('sortnames') == "Sort by name":
        name_list = Person.objects.order_by('name')[0:]
    elif request.GET.get('search'):
        name_list = Person.objects.filter(name=request.GET.get('search'))
        if len(name_list) == 0:
            messages.error(request, "Search is case sensitive.")

    context = {
        'name_list': name_list,
    }

    return render(request, 'names/names.html', context)


def upload_view(request):
    try:
        uploaded_file = None

        if request.method == 'POST':
            uploaded_file = request.FILES['json']
            # if uploaded file is JSON
            if uploaded_file.content_type == "application/json":

                # write uploaded file to names.json
                save_uploaded_file(request.FILES['json'])

                # First read JSON-file and get the data.
                # Then parse data and add persons to database.
                add_names_to_database(read_names_json())
    except KeyError:
        print("Error handling the uploaded file. No file was given.")

    context = {
        'uploaded_file': uploaded_file

    }
    return render(request, 'upload/upload.html', context)


def save_uploaded_file(f):
    with open('names.json', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def read_names_json():
    with open('names.json', 'r') as f:
        data = json.load(f)

    pprint(data)
    return data


def add_names_to_database(data):
    # in json-file go through every person in list "names"
    for person in data["names"]:
        # if person doesnt exist, add person.
        if not Person.objects.filter(name=person["name"], amount=person["amount"]).exists():
            person_obj = Person(name=person["name"], amount=person["amount"])
            print(person_obj)
            person_obj.save()
