from views import newEmployee
from django.conf.urls import url


urlpatterns = [
    
    url(r'^add-employee/$', newEmployee, name='admin'),
]