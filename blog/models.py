from django.db import models

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
