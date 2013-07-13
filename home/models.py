from django.db import models
import string

class NavItem(models.Model):
	name = models.CharField(max_length=32)
	url = models.CharField(max_length=1024)
	ordering = models.IntegerField(default=0)
	parent = models.ForeignKey('self', null=True, blank=True)
	def display_text(self):
		if self.url[:7] == "http://" or self.url[:8] == "https://":
			return string.upper(self.name) + '<img style="padding-left:3px; margin-top:-6px; opacity: 0.5;" src="http://i.imgur.com/EB4X3nv.png" />'
		return string.upper(self.name)
		

class homepageFeature(models.Model):
	title = models.CharField(max_length=32)
	url = models.CharField(max_length=1024)
	imgurl = models.CharField(max_length=1024)
	ordering = models.IntegerField(default=0)
	description = models.CharField(max_length=1024)

class HeaderImage(models.Model):
	reference = models.CharField(default="Untitled", max_length=64)
	imgurl = models.CharField(max_length=1024)
	precedence = models.IntegerField(default=0)
	view_name = models.CharField(max_length=128, null=True, blank=True)
	date_start = models.DateTimeField(default=None, null=True, blank=True)
	date_end = models.DateTimeField(default=None, null=True, blank=True)

class SidebarItem(models.Model):
	title = models.CharField(max_length=32)
	content = models.TextField()
