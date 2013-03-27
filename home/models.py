from django.db import models


class NavItem(models.Model):
	name = models.CharField(max_length=32)
	url = models.CharField(max_length=1024)
