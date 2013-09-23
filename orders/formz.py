from django import forms
from .models import OrderItem,Order
from django.forms import ModelForm, TextInput
#import datetime
#import re
class CheckoutForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ('created_by','modified_by','is_active','status','restaurant')
		
#----------------------------------------------------------------------------------

class PartialOrderItemForm(ModelForm):
	class Meta:
		model = OrderItem
		exclude = ('shopping_id','is_active','modified_by','created_by','item','order')
		widgets = {
			'quantity': TextInput(attrs={'size':'2','value':'0', 'class':'quantity','maxlength':'5'}),
#			'item_slug': forms.HiddenInput(),
		
#	error_messages={'invalid':'please enter a valid quantity.'},min_value=0),
		}
class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea())
