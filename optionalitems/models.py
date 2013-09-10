from django.db import models
from smartmin.models import SmartModel
from restaurant_detail.models import Restaurant
# Create your models here.

class Optional_Item(SmartModel):
	 """Optional items that belong to an item"""
	 
	 name = models.CharField(max_length=20, help_text="Item name.")
	 price = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True,help_text="if item has no price indicate 0.00")
	 description = models.CharField(max_length=200,help_text="Describe item in few words")
	 owner = models.ForeignKey(Restaurant)
	 
	 def __unicode__(self):
		return "%s" % (self.name + " " + str(self.price))
class OptionalItemCategory(SmartModel):
	"""Category to which optional items belong"""
	
	title = models.CharField(max_length=20,help_text="Category name")
	optional_items = models.ManyToManyField(Optional_Item)
	display_order = models.IntegerField(max_length=3,help_text="In what order should the categories appear")
	owner = models.ForeignKey(Restaurant)
	
	def __unicode__(self):
		return u"%s (%s)" % (self.title, u", ".join([item.name for item in self.optional_items.all()]))
	
class ToppingsAndExtras(SmartModel):
	name = models.CharField(max_length= 140,)
	price = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True, help_text="if item has no price indicate 0.00")
	description = models.CharField(max_length=140, null=True,blank=True)
	
	def __unicode__(self):
		return "%s" % (self.name)
	
class ToppingsAndExtrasCategory(SmartModel):
	title = models.CharField(max_length=20, help_text="Category Title")
	toppings_and_extras= models.ManyToManyField(ToppingsAndExtras)
	display_order = models.IntegerField(max_length=3, help_text="In what order should the categories appear")
	owner = models.ForeignKey(Restaurant)
	
	def __unicode__(self):
		return u"%s (%s)" % (self.title, u", ".join([item.name for item in self.toppings_and_extras.all()]))
