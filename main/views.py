from django.views.generic.edit import FormView
from main import forms
from django.http import HttpResponseRedirect

# our first class-based view definition

class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/" # it is used by form_valid(form) to render on success

    def form_valid(self, form):
        form.send_mail()
        HttpResponseRedirect(self.success_url)
        # return super().form_valid(form) # after validation, render success url