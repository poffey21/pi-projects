from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.ConnectView.as_view(), name='connect_home'),
]

