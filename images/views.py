from django.shortcuts import render, redirect
from .forms import ImageCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages




# Create your views here.
@login_required
def image_create(request):
    if request.method == "POST":
        form = ImageCreateForm(data = request.POST)
        if form.is_valid():
            #Form data is valid
            cd = form.cleaned_data
            new_image = form.save(commit = False)

            #assign current user to the form
            new_image.user = request.user
            new_image.save()
            messages.success(request, "Image added successfully!")

            #redirect the user to the detail view of the image:
            return redirect(new_image.get_absolute_url())

    #If the form is not valid
    else:
        form = ImageCreateForm(data = request.GET)

    return render(
        request,
        "images/image/create.html",
        {'section':"images", "form":form})