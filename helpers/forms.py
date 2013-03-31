from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


class RegistrationFormView(FormView):
    form_class = UserCreationForm
    template_name = "registration/registration_form.html"

    def form_valid(self, form):
        user = form.save()
        user = authenticate(
            username=self.request.POST['username'],
            password=self.request.POST['password2'])
        login(self.request, user)
        self.success_url = self.request.GET['next']
        return super(RegistrationFormView, self).form_valid(form)
