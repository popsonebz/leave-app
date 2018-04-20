from django.contrib.auth import views as auth_views
from views import leave, employee
from django.conf.urls import url
from django.core.urlresolvers import reverse

urlpatterns = [
    url(
        r'^login/$',
        auth_views.login,
        name='login',
        kwargs={'template_name': 'login.html'}
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        name='logout',
        kwargs={'next_page': '/leave/login/'}
    ),
    url(
        r'^apply/$',
        leave,
        name='leave',
    ),
]

