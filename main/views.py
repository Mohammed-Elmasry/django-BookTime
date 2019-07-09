from django.views.generic.edit import FormView
from main import forms


# our first class-based view definition

class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/" # it will redirect to main page if successful

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)