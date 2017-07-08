# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from . import utils


class ConnectView(generic.TemplateView):
    """ Enables users to see what connections are available  """
    template_name = "connect/home.html"

    def get_context_data(self, **kwargs):
        context = super(ConnectView, self).get_context_data(**kwargs)
        context['ssid_list'] = utils.scan('wlan0')
        return context
