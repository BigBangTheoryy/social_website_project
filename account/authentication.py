from django.contrib.auth.models import User
from account.models import Profile

class EmailAuthBackend:
    "Authenitcate using email addreess"

    def authenticate(self, request, username =  None, password = None):# "authenticate" is the in-built function name set by django

        try:
            user = User.objects.get(email = username)
            if user.check_password(password):
                return user
            return None

        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk = user_id)

        except User.DoesNotExist:
            return None


def create_profile(backend, user, *args, **kwargs):
    "Create User Profile for Socail Auth"

    Profile.objects.get_or_create(user = user)


