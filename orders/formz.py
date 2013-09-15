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


#______________________________________________________not needed for now# generates a list of years that we can use for our credit card expiration year dropdown
#def cc_expire_years():
#	current_year = datetime.datetime.now().year
#	years = range(current_year, current_year+12)
#	return [(str(x),str(x)) for x in years]

# creates list of months
#def cc_expire_months():
#	months= []
#	for month in range(1,13):
#		if len(str(month)) == 1:
#			numeric  = '0' + str(month)
#		else:
#			numeric = str(month)
#		months.append((numeric, datetime.date(2013,month, 1).strftime('%B')))
#	return months

#tuple that contains the type of cards our site will accept.

#CARD_TYPES = (
#	('VISA','VISA'),
#	('Mastercard','Mastercard'),
#	('AMEX','AMEX'),
#	('Discover','Discover'),
#)

##takes string,strips out all characters that arent numbers.we use python regular expression module, finding all non numeric digits and replacing them with an empty string. we use this when validating credit cards.
#def strip_non_numbers(data):
#	""" gets rid of all non-number characters"""
#	non_numbers = re.compile('\D')
#	return non_numbers.sub('',data)

#Gateway test credit cards wont pass this validation
#def cardLuhnChecksumValid(card_number):
#	""" checks to make sure that the card passes a luhn mod-10 checksum """
#	sum = 0
#	num_digits = len(card_number)
#	oddeven = num_digits & 1
#	for count in range(0, num_digits):
#		digit = int(card_number[count])
#		if not (( count & 1) ^ oddeven ):
#			digit = digit * 2
#		if digit > 9:
#			digit = digit - 9
#		sum = sum + digit
#	return ( (sum % 10) == 0)

#class CheckoutForm(forms.ModelForm):
#	def __init__(self,*args,**kwargs):
#		super(CheckoutForm, self).__init__(*args, **kwargs)
		#overide default attributes
#		for field in self.fields:
#			self.fields[field].widget.attrs['size'] = '30'
#		self.fields['credit_card_type'].widget.attrs['size'] ='1'
#		self.fields['credit_card_expire_year'].widget.attrs['size'] = '1'
#		self.fields['credit_card_expire_month'].widget.attrs['size'] = '1'
#		self.fields['credit_card_cvv'].widget.attrs['size'] = '5'
#	class Meta:
#		model = Order
#		exclude = ('status','transaction_id','billing_country','created_by','modified_by','restaurant',)
		
#	credit_card_number = forms.CharField()
#	credit_card_type = forms.CharField(widget=forms.Select(choices=CARD_TYPES))
#	credit_card_expire_month = forms.CharField(widget=forms.Select(choices=cc_expire_months()))
#	credit_card_expire_year = forms.CharField(widget=forms.Select(choices=cc_expire_years()))
#	credit_card_cvv = forms.CharField()
	
#	def clean_credit_card_number(self):
#		cc_number = self.cleaned_data['credit_card_number']
#		stripped_cc_number = strip_non_numbers(cc_number)
#		if not cardLuhnChecksumValid(stripped_cc_number):
#			raise forms.ValidationError('The credit card you entered is invalid.')
	
