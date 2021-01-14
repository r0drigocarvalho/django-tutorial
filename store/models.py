from django.db import models
from django.urls import reverse

class Produto(models.Model):

	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	body  = models.TextField()
	image = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	

	class Meta: 
		ordering = ("-created",)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("store:detail", kwargs={"slug": self.slug})