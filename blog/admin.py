__author__ = 'payload'

from django.contrib import admin
from djworks.blog.models import Category


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ['title']}
	# the content of slug be from the title field, can be changed if needed!

admin.site.register(Category, CategoryAdmin)