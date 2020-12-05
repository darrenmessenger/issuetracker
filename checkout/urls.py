from django.conf.urls import url, include
from .views import checkout

urlpatterns = [
    url(r'^$',  checkout, name="checkout")
    ]