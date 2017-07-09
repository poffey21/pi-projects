# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from .utils import Wireless


class ConnectView(generic.TemplateView):
    """ Enables users to see what connections are available  """
    template_name = "connect/home.html"

    def get_context_data(self, **kwargs):
        context = super(ConnectView, self).get_context_data(**kwargs)
        wifi = Wireless('wlan0')
        context['ssid_list'] = wifi.scan()
        return context


class FormView(generic.TemplateView):
    
    template_name = "vendor/bootstrap_login.html"
