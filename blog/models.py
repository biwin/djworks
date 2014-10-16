from django.db import models
import datetime
from django.contrib.auth.models import User
from markdown import markdown


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
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = (
		(LIVE_STATUS, 'Live'),
		(DRAFT_STATUS, 'Draft'),
		(HIDDEN_STATUS, 'Hidden'),
	)
	title = models.CharField(max_length=250)
	excerpt = models.TextField(blank=True)
	body = models.TextField()
	slug = models.SlugField(unique_for_date='pub_date')
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	author = models.ForeignKey(User)
	enable_comments = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
	categories = models.ManyToManyField(Category)
	excerpt_html = models.TextField(editable=False, blank=True)
	body_html = models.TextField(editable=False, blank=True)

	class Meta:
		verbose_name_plural = 'Entries'
		ordering = ['-pub_date']

	def __unicode__(self):
		return self.title

	def save(self, force_insert=False, force_update=False):
		self.body_html = markdown(self.body)

		if self.excerpt:
			self.excerpt_html = markdown(self.excerpt)
		super(Entry, self).save(force_insert, force_update)

	def get_absoulte_url(self):
		return '/weblog/%s/%s/' % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)