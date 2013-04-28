from django.db import models
from smartmin.models import SmartModel
from tempfile import mktemp
import os
from django.core.files import File
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from djangoratings import AnonymousRatingField

	
class Restaurant_detail(SmartModel):
	# Official details of restaurants.
	#FOOD_TYPE=(
	#	('FF', 'FastFood'),
	#	('JB', 'Juicebar'),
	#	('BF', 'Buffet'),
		
	#)
	
	DAYS=(
		('SDW','Seven days a week'),
		('AWUS','All Weekdays,untill Saturday'),
		('OWD','Only in the weekdays'),
	)
	
	
	SERVICES=(
		('DELIVERY', 'Delivery'),
		('PICKUP', 'PickUp'),
	)
	first_name=models.CharField(max_length=64,help_text="Your first name.")
	last_name=models.CharField(max_length=64,help_text="Your last name")
	address=models.CharField(max_length=100,help_text="e.g Klab Restaurant,6th floor Telecom house,Kacyiru")
	#city=models.Charfield(max_length=25,help_text="e.g Kigali")
	mobile= PhoneNumberField(max_length=18,help_text="Highly recommended, should include country code e.g 25078######")
	email=models.EmailField(max_length=74,help_text="Higly recommended")
	restaurant_name =models.CharField(max_length=100, help_text="Please provide name of your restaurant")
	logo=models.ImageField(max_length=500,null=True,blank=True,upload_to="restaurant_detail/restaurant_detail", help_text = "upload your restaurant logo")
	cusine=models.TextField(help_text="Type(s)/Cusine(s) of Food served")
	service_type=models.CharField(max_length=15,choices=SERVICES,help_text="Do you Deliver,offer Pickup services or both")
	service_fee=models.IntegerField(max_length=5,null=True,blank=True,help_text="How much you charge for delivery and pickup services")
	service_days=models.CharField(max_length=5,choices=DAYS, help_text= "Days on which you offer delivery/pickup services")
	service_hours_start=models.TimeField(auto_now=False,auto_now_add=False,help_text="Time when your delivery services start i.e HH:MM,don't include am or pm.")
	service_hours_end=models.TimeField(auto_now=False,auto_now_add=False,help_text="Time when your delivery services end i.e HH:MM, don't include am or pm.")
	minimum_order_amount =models.IntegerField(max_length=5,help_text="The least amount you accept for online ordering")
	delivery_territory = models.TextField(help_text="places where you will deliver e.g, kacyiru,kimihurura,kigali city centre..")
#	delivery_hours=models.DateTimeField()
	def __unicode__(self):
		return "%s %s %s %s %s %s %s %s" % (self.restaurant_name,self.cusine,self.service_type,self.first_name, self.last_name, self.restaurant_name, self.address, self.mobile)

# repeating the above model but changing model name..
class Restaurant(SmartModel):
	# Official details of restaurants.
	#FOOD_TYPE=(
	#	('FF', 'FastFood'),
	#	('JB', 'Juicebar'),
	#	('BF', 'Buffet'),
		
	#)
	DAYS=(
		('SDW','Seven days a week.'),
		('AWUS','All weekdays untill saturday'),
		('OWD','Only in the weekdays'),
	)
	
	SERVICES=(
		('DELIVERY', 'Delivery'),
		('PICKUP', 'PickUp'),
	)
	user=models.ForeignKey(User,default=1)
#	piglet=models.CharField(max_length=5,null=True,blank=True,help_text='oink,oink')
	first_name=models.CharField(max_length=64,help_text="Your first name.")
	last_name=models.CharField(max_length=64,help_text="Your last name")
	address=models.CharField(max_length=100,help_text="e.g Klab Restaurant,6th floor Telecom house,Kacyiru")
	#city=models.Charfield(max_length=25,help_text="e.g Kigali")
	mobile= PhoneNumberField(max_length=18,default='+25078######',help_text="Highly recommended, should include country code e.g 25078######")
	email=models.EmailField(max_length=74,help_text="Higly recommended")
	restaurant_name =models.CharField(max_length=100, help_text="Please provide name of your restaurant")
	logo=models.ImageField(max_length=500,null=True,blank=True,upload_to="restaurant_detail/restaurant/", help_text = "upload your restaurant logo")
	cusine=models.TextField(help_text="Type(s)/Cusine(s) of Food served")
	service_type=models.CharField(max_length=15,choices=SERVICES,help_text="Do you Deliver,offer Pickup services.")
	service_fee=models.IntegerField(max_length=5,null=True,blank=True,help_text="HOw much you charge for delivery or pickup service.")
	service_days=models.CharField(max_length=5,choices=DAYS,null=True,blank=True,help_text= "Days on which you offer delivery/pickup services")
	service_hours_start=models.TimeField(auto_now=False,auto_now_add=False,help_text="Time when your services start i.e HH:MM, don't include am or pm.")
	service_hours_end=models.TimeField(auto_now=False,auto_now_add=False,help_text="Time when your  services end i.e HH:MM,don't include am or pm.")
	minimum_order_amount =models.IntegerField(max_length=5,default='1',help_text="The least amount you accept for online ordering")
	delivery_territory = models.TextField(help_text="places where you will deliver e.g, kacyiru,kimihurura,kigali city centre..")
	token=models.CharField(max_length=32, unique=True, help_text="token used to activate account")
	restaurant_detail=models.ForeignKey(Restaurant_detail,default='1',help_text="the initial application of the restaurant_details of restaurant")
	rating = AnonymousRatingField(range=5, weight=10,allow_anonymous = True,use_cookies= True)# 5 possible rating values, 1-5 and weight of 10 
#	delivery_hours=models.DateTimeField()
	def __unicode__(self):
		return "%s %s %s %s %s %s %s %s" % (self.restaurant_name,self.cusine, self.service_type,self.first_name, self.last_name, self.restaurant_name, self.address, self.mobile)	


	def update_restaurant_logo(self):
		pic = self.restaurant_detail.logo
		
		if pic:
			tmp_name = mktemp()
			tmp_file= open(tmp_name, 'wb')
			tmp_file.write(str(pic.file.read()))
			tmp_file.close()
			
			tmp_file = open(tmp_name, 'r')
			self.logo.save('%s.jpg' % self.restaurant_detail, File(tmp_file), save=True)
			self.save()
			
			os.unlink(tmp_name)
			
	def get_password(self):
		return user.password
# Create your models here.
# note that this is items...
class Item(SmartModel):
	#restaurant_name=models.CharField(max_length=100,help_text="please provide name of your restaurant")
	name= models.CharField(max_length=64,help_text="Name for this item e.g Hamburger")
	description= models.CharField(max_length=200,help_text="Describe the item in a few words e.g Ham with bread")
	display_order=models.IntegerField(max_length=3,help_text="in what order should items appear")
	price=models.DecimalField(max_digits=9,decimal_places=2)
	owner = models.ForeignKey(Restaurant,help_text="Owner of an item")
#	slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
	
	
	class Meta:
		db_table='items'
		verbose_name_plural = 'items'

	def __unicode__(self):
		return "%s %s" % (self.name,self.owner)
#	def get_absolute_url(self):
#		return('menu_items', (),{'menu_items':self.slug})
#		return()

# Create your models here.

class Category(SmartModel):
	item=models.ManyToManyField(Item)
	title=models.CharField(max_length=64,help_text="Title of category e.g BreakFast")
	description=models.CharField(max_length=64,help_text="Describe the category e.g the items included in the category")
	display_order=models.IntegerField(max_length=3,help_text="in what order should categories appear")
	owner = models.ForeignKey(Restaurant,related_name='category',help_text="owner of category")

	
	class Meta:
		db_table = 'categories'
		verbose_name_plural = 'Categories'


	def __unicode__(self):
		return "%s %s %s %s %s" % (self.item, self.title,self.display_order,self.description, self.owner)






	
	

	

