from django.template.response import TemplateResponse
from django.views.generic import FormView, TemplateView

from forms import SetEmailForm


class AccountView(TemplateView):
    """Class based view used to call get access to user's account"""
    template_name = "account.html"


class MailEditView(FormView):
    """Class based view used to manage user's email update"""
    template_name = "mail_edit.html"
    form_class = SetEmailForm

    def get_form_kwargs(self):
        form_kwargs = super(MailEditView, self).get_form_kwargs()
        form_kwargs.update({'initial': {'email': self.request.user.email}})

        return form_kwargs

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return TemplateResponse(request, self.template_name, context=context)
