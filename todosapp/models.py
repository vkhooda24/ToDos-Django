from __future__ import unicode_literals

from django.db import models

class NotesList(models.Model):
	title = models.CharField(max_length = 30)
	desc  = models.CharField(max_length = 30)
	author= models.CharField(max_length =30)
