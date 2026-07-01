from django import forms
from .models import Image
import requests
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageFormCreation(forms.ModelForm):
    class Meta:
        model    = Image
        fields    = ['title', 'url', 'decription']
        widgets = {
            'url': forms.HiddenInput,
        }


    def clean_url(self): #Checking if the url is of valid extension or not
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extensions = url.rsplit(".", 1)[1].lower()
        if extenstions not in valid_extensions:
            raise forms.ValidationError("Not compatible file format. Please valid format!")

        return url


    def save(self, force_insert = False,  force_update = False, commit = True):
        image = super().save(commit = False) # A new image instance is created by calling the save() method

        image_url = self.cleaned_data['url']#The URL of the image is retrieved from the cleaned_data dictionary of the form.

        name = slugify(image.title)
        extension = image_url.rsplit(".", 1)[1].lower()
        image_name = f'{name}.{extension}'

        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save = False)

        if commit:
            image.save()

        return image

