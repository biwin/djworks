__author__ = 'payload'

from django.contrib import admin
from djworks.blog.models import Category


class CategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Category,CategoryAdmin)