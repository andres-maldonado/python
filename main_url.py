#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('irc.apps.website.urls')),
    # url(r'^', include('wild_unit.apps.user_profile.urls')),
    #url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    #url(r'^7205846B147B4F20E2FAF76A31D8C864\.txt/$', TemplateView.as_view(template_name='7205846B147B4F20E2FAF76A31D8C864.txt', content_type='text/plain')),
    # SLUG
    # url(r'^', include('wild_unit.apps.blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
