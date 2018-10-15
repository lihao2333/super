from django.conf.urls import url
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^skill/$', views.skill, name="skill"),
    url(r'^resume/$', views.resume, name="resume"),
]