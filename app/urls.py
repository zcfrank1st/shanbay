# -*- coding: utf-8 -*-
__author__ = 'zcfrank1st'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^save/configs$', views.save_configs),
    url(r'^load/configs/(?P<user_id>\d+)/$', views.load_configs),
    url(r'^load/words/(?P<user_id>\d+)/$', views.load_words_through_configs),
    url(r'^save/note$', views.save_note),
    url(r'^see/notes/(?P<word_id>\d+)/$', views.see_open_notes),
    url(r'^save/and/share$', views.save_and_open_note),
    url(r'^learned/words$', views.mark_learned_words),
]
