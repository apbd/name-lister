from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from .forms import PersonForm

from .models import Person

import json
from pprint import pprint


def names_view(request, *args, **kwargs):
    name_list = Person.objects.all()
    print("yes", request.GET.get('search'))

    # what table order/sort is needed
    # if server receives get request named "sortamount"
    if request.GET.get('sortamount'):
        # order name_list by amount (prefix '-' for descending)
        name_list = Person.objects.order_by('-amount')

    elif request.GET.get('sortnames'):
        name_list = Person.objects.order_by('name')

    elif request.GET.get('search'):
        name_list = Person.objects.filter(name=request.GET.get('search'))
        if len(name_list) == 0:
            messages.error(request, "Search is case sensitive.")

    # Total names counter
    total_names = len(name_list)
    if total_names == 0:
        messages.error(request, "No names found.")

    context = {
        'name_list': name_list,
        'total_names': total_names
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
                try:
                    add_names_to_database(read_names_json())
                except:
                    messages.error(request, "Adding names to database failed. Problem with file. "
                                            "Expected JSON-file with list named 'names'.")

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
    try:
        with open('names.json', 'r') as f:
            data = json.load(f)

        pprint(data)
    except:
        print("Reading names from JSON-file failed.")
        return None

    return data


def add_names_to_database(data):
    # in json-file go through every person in list "names"
    for person in data["names"]:
        # if person doesnt exist, add person.
        if not Person.objects.filter(name=person["name"], amount=person["amount"]).exists():
            person_obj = Person(name=person["name"], amount=person["amount"])
            print(person_obj)
            person_obj.save()


