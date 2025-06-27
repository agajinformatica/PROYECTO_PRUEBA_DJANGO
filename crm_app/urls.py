from django.urls import path
from .views import crm_view

urlpatterns = [
    path("", crm_view, name="crm_view"),
]
