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