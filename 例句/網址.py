# -*- coding: utf-8 -*-
from django.conf.urls import url
from 例句.介面.看例句 import 看

urlpatterns = [
    url(r'^看/$', 看),
]
