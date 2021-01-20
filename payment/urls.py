from django.urls import path
from django.urls.resolves import URLPattern
from . import views

urlpatterns = [
        path("test", views.index, name="index")
]
