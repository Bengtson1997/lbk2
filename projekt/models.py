from django.db import models
from django.urls import reverse
# Create your models here.

class projekt(models.Model):
	dato						= models.TextField(blank=False, null=False)
	titel 						= models.TextField(blank=False, null=False)
	timer 						= models.TextField(blank=False, null=False)
	ekstra_timer 				= models.TextField(blank=True, null=True)
	ekstra_timer_beskrivelse	= models.TextField(blank=True, null=True)
	kørsel						= models.TextField(blank=False, null=False)
	opgave_beskrivelse 			= models.TextField(blank=False, null=False)
	materialer					= models.TextField(blank=False, null=False)

	def get_absolute_url_detail(self):
		return reverse("projekt:projekt_detaljer", kwargs={"my_id": self.id})