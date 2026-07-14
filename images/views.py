from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST

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


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug) # View taking slug here as a parameter because it will be used in the URL, so we have to confirm the slug as well here itself

    return render(request, "images/image/detail.html", {"section": "images",  "image": image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get("id")
    action = request.POST.get("action")

    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == "like":
                image.users_like.add(request.user)

            else:
                image.users_like.remove(request.user)

            return JsonResponse({"status":"ok"})

        except Image.DoesNotExist:
            pass

    return JsonResponse({"status":"error"})








