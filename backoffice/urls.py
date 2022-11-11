from django.conf.urls import url

from backoffice.views import common

urlpatterns = [
    url(r'^$', common.home, name='home'),
    url(r'^login/$', common.login, name='login'),
    url(r'^logout/$', common.log_out, name='logout'),
    url(r'^logged_out/$', common.logged_out, name='logged_out'),
]
