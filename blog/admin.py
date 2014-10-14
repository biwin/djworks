__author__ = 'payload'

from django.contrib import admin
from djworks.blog.models import Category, Entry


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ['title']}
	# the content of slug be from the title field, can be changed if needed!


class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ['title']}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)