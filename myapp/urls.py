from django.conf.urls import url
from . import views


app_name = 'myapp'
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
]
