from __future__ import unicode_literals

from django.db import models

class Estado(models.Model):
	nombre_estado = models.CharField(max_length = 45)

	def __str__(self):
		return self.nombre_estado

	def __unicode__(self):
		return self.nombre_estado