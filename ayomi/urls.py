from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout

from ayomi import settings
from user_management import views as auth_views

urlpatterns = [
    url(r"^login/", login, {"template_name": "login.html"}),
    url(r"^account/", login_required(auth_views.AccountView.as_view()), name='account'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r"^mail_edit/", login_required(auth_views.MailEditView.as_view()), name='mail_edit'),
]
