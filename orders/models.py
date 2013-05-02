from django.db import models
from smartmin.models import SmartModel
#from django import forms
import decimal
from phonenumber_field.modelfields import PhoneNumberField
#from cart.models import OrderItem
from restaurant_detail.models import Restaurant,Item
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('augment_quantity','name','price','total',)

# Create your models here.

	
#class Customer(SmartModel):
	#contact info
#	email = models.EmailField(max_length=50,help_text="Needed as alternative")
#	mobile = PhoneNumberField(max_length=20,default='+25078######',help_text="Needed to communicate and confirm payment from mobile money")
	
	#billing information
#	billing_name= models.CharField(max_length=50,help_text="Needed so we can deliver to the right individual")
#	billing_address= models.CharField(max_length=50,help_text="Needed for delivery purposes, should be office address.")	
#	billing_city = models.CharField(max_length=50,help_text="F4L services are only in selected cities.")

		
#	def __unicode__(self):
#		return "%s %s %s %s %s" % (self.email,self.mobile,self.billing_name,self.billing_address,self.billing_city)

class OrderItem(SmartModel):
	"""model to store information of the item instance in customers online_order"""
	shopping_id = models.CharField(max_length=255,db_index=True)
#	date_added = models.DateTimeField(auto_now_add=True)
	quantity = models.IntegerField()
	item = models.ForeignKey(Item)
#	item_slug = models.CharField(max_length=50)


	class Meta:
		db_table='order_items'
		
	def __unicode__(self):
		return " %s %s" % (self.quantity,self.item)
	@property
	def total(self):
		return self.quantity *self.item.price * self.item.owner.service_fee
	@property
	def name(self):
		return self.item.name
	@property
	def price(self):
		return self.item.price

	def augment_quantity(self,quantity):
		self.quantity = self.quantity + int(quantity)
		self.save()



class Order(SmartModel):
	"""model to store each item instance """
	#each individual status
	SUBMITTED = 1 # the credit card was valid or mobilemoney was recieved.It is ready for us to process the order
	PROCESSED = 2 # After submitted orders are reviewed, we can mark them as processed, letting deliverers know order is ready to be shipped
	DELIVERED = 3 # the order has been processed and approved by the adminstrator(in this case us), it is delivered.
	PICKED_UP =4 # the order has been processed and is picked up by customer
	CANCELLED = 5 # Customer called the company and decided they didnt want to go through with the order either by phone or email.
	
	# SET OF POSSIBLE STATUSES
	ORDER_STATUSES = ((SUBMITTED,'Submitted'),(PROCESSED,'Processed'),(DELIVERED,'Delivered'),(PICKED_UP,'picked_up'),(CANCELLED,'Cancelled'),)
	#Order info
	date = models.DateTimeField(auto_now=True,auto_now_add=True)
	status = models.IntegerField(choices=ORDER_STATUSES, default=SUBMITTED)
#	customer = models.ForeignKey(Customer,null=True,blank=True,help_text="The customer who made this order",default=None,)
	restaurant = models.ForeignKey(Restaurant,null=True,blank=True,default = None,help_text="The restaurant the customer order from")
	#contact info
#	email = models.EmailField(max_length=50,help_text="Needed as alternative")
	mobile = PhoneNumberField(max_length=20,null=True,blank=True,help_text="For confirmation purposes..")
	
	#billing information
	name= models.CharField(max_length=50,null=True,blank=True,help_text="Needed so that we can deliver to the right individual")
	address = models.CharField(max_length=50,null=True,blank=True,help_text="Where do we find you. e.g Klab 6th floor,Telecom House,Kacyiru")
	city = models.CharField(max_length=50,null=True,blank=True,help_text="F4L services are only in Kigali.")
	additional_information = models.TextField(max_length=250,null=True,blank=True,help_text="Anything more we should know...")
#	total_amount = models.integerField(max_length=6,defaulrhelp_text="Amount paid by customer F4L")

		
	def __unicode__(self):
		return "%s %s %s %s" % (self.name,self.address,self.city,self.additional_information)
		
	@property
	def total(self): 
		total = decimal.Decimal('0.00')
		order_items = OrderItem.objects.filter(order=self)
		for item in order_items:
			total += item.total
		return total

class Recieved_Order(SmartModel):
	item = models.ForeignKey(Item)
	date_added = models.DateTimeField(auto_now=True,auto_now_add=True)
	quantity = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=9,decimal_places=2)
	order = models.ForeignKey(Order)
	
	def __unicode__(self):
		return unicode(self.order)
	
	@property
	def total(self):
		return self.quantity * self.price    
	@property
	def name(self):
		return self.product.name




#class OrderItems(SmartModel):
#	order_items = models.ForeignKey(OrderItem)
#	quantity = models.IntegerField(default=0)
#	price = models.DecimalField(max_digits=9,decimal_places = 2)
#	orders = models.ForeignKey(Orders)
	
#	def __unicode__(self):
#		return "%s %s %s" % (self.order_items,self.orders)
	
#	@property
#	def total(self):
#		return self.quantity *self.price
#	@property
#	def name(self):
#		return self.item.name
		
		
