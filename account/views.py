from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


# User Login View
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username =  cd['username'], password = cd['password'])


            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Login Successful")

                else:
                    return HttpResponse("Account not active")

            else:
                return HttpResponse("Invalid Credentials")
    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})

@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section":"dashboard"})



#User Registration:

def register(request):
    #Check if method is POST
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        #Check if form is valid
        if user_form.is_valid():

            #Create New User:
            new_user = user_form.save(commit = False) # Not saving in DB just yet

            new_user.set_password(user_form.cleaned_data['password']) #set_password() method of the user model. This method handles password hashing before storing the password

            #Save the user:
            new_user.save()

            Profile.objects.create(user = new_user) #After the new user is saved, the profile will be created automatically.

            return render(request, "account/register_done.html", {"new_user": new_user})


    else: # If the form is invalid:
        user_form = UserRegistrationForm() #open the form again

    return render(request, "account/register.html", {"user_form": user_form})



#Edit Form

@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance = request.user, data = request.POST)

        profile_form = ProfileEditForm(instance = request.user.profile, data = request.POST, files = request.FILES) #Django automatically creates a reverse relationship for a OneToOneField. Therefore, if Profile has user = OneToOneField(User), you can access the related profile using user.profile.Since request.user is the currently logged-in User object, request.user.profile returns the Profile associated with that user.


        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            #Showing success after the profile is edited successfully
            messages.success(request, "Profile updated successfully!")

        else:
            messages.error(request, "Error occured during saving. Please try again!")

    else:
        user_form    = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)


    return render(request, "account/edit.html", {"user_form": user_form, "profile_form": profile_form })
































