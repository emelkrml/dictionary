# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.contrib import admin
from django import forms
from .models import Category, Topic, Entry, User

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    search_fields = ('title',)
    list_filter = (
        ('user', admin.RelatedOnlyFieldListFilter),
    )
    filter_horizontal = ('category',)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    #list_display = ('user',)
    list_display = ('title', 'content')
    search_fields = ('title',)


