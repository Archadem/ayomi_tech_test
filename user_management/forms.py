"""File used to manage custom forms"""

from django.forms import EmailField, forms


class SetEmailForm(forms.Form):
    """
    A basic form to allow user's email update
    """
    email = EmailField()

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(SetEmailForm, self).__init__(*args, **kwargs)

    def save(self):
        """Method used to save new user's mail"""
        user = self.request.user
        user.email = self.cleaned_data['email']

        user.save()
        return user
