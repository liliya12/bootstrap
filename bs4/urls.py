from django.urls import path
from . import views

urlpatterns = [
    path("", views.index1, name="index1"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("contactus",views.contactus,name="contactus")
]