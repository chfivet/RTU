from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from backoffice.views import common

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('backoffice.urls')),
]
