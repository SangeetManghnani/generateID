__author__ = 'sangeet'

from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^register/',views.register, name='register'),
    url(r'^generate/', views.generate, name = "generate")
]