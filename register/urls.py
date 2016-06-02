
from django.conf.urls import include, url
from django.contrib import admin
from register import views
from register.views import *
from register.models import *

urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),

]
