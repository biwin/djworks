from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
	title = models.CharField(max_length=250, help_text='Max 250 chars.')
	slug = models.SlugField(unique=True, help_text='Generated automatically from the title, needs to be unique')
	description = models.TextField()

	class Meta:
		ordering = ['title']
		verbose_name_plural = 'Categories'

	def get_absolute_url(self):
		return "/categories/%s/" % self.slug

	def __unicode__(self):
		return self.title


class Entry(models.Model):
	title = models.CharField(max_length=250)
	excerpt = models.TextField(blank=True)
	body = models.TextField()
	slug = models.SlugField(unique_for_date='pub_date')
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	author = models.ForeignKey(User)
	enable_comments = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	class Meta:
		verbose_name_plural = 'Entries'

