from django.contrib.auth.forms import AuthenticationForm

from backoffice.models import Discipline

from django.contrib.auth.forms import UserCreationForm


def default(request):
    return {
        'disciplines': Discipline.objects.all(),
        'login_form': AuthenticationForm(),
        'path': request.path,
        'registration_form': UserCreationForm()
    }
