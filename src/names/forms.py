from django.forms import ModelForm
from .models import Person, UploadJsonFile


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class UploadJsonFileForm(ModelForm):
    class Meta:
        model = UploadJsonFile
        fields = '__all__'