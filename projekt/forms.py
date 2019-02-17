from django import forms

from .models import projekt

class ProjektForm(forms.ModelForm):
	class Meta:
		model = projekt
		fields = [
			'dato',
			'titel',
			'timer',
			'ekstra_timer',
			'ekstra_timer_beskrivelse',
			'kørsel',
			'opgave_beskrivelse',
			'materialer'
		]

class RawProjektForm(forms.Form):
	dato						= forms.CharField(widget=forms.Textarea)
	titel 						= forms.CharField(widget=forms.Textarea)
	timer 						= forms.CharField(widget=forms.Textarea)
	ekstra_timer 				= forms.CharField(required=False, widget=forms.Textarea)
	ekstra_timer_beskrivelse	= forms.CharField(required=False, widget=forms.Textarea)
	kørsel 						= forms.CharField(widget=forms.Textarea)
	opgave_beskrivelse 			= forms.CharField(widget=forms.Textarea)
	materialer					= forms.CharField(widget=forms.Textarea)	