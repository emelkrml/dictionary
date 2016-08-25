# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.contrib import admin
from django import forms
from .models import Category, Baslik, Entry

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Baslik)
class BaslikAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    search_fields = ('title',)
    #list_filter = ('user', admin.RelatedOnlyFieldListFilter)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)
