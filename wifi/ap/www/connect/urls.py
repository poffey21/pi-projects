from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.ConnectView.as_view(), name='connect_home'),
    url(r'^form/$', views.FormView.as_view(), name='connect_form'),
]

