# Create your views here.
from .models import *
from smartmin.views import *
from django.contrib.auth.models import User
from django import forms
from restaurant_detail.models import Restaurant


#class CustomerCRUDL(SmartCRUDL):
#	model = Customer
#	actions = ('list','read','create')
#	permissions = True
	
#	class Create(SmartCreateView):
#		fields = ('email','mobile','billing_name','billing_address','billing_city')
		
#	class List(SmartListView):
#		fields = ('email','mobile','billing_name','billing_address','billing_city')
		
#		def get_queryset(self,*args,**kwargs):
#			queryset=super(CustomerCRUDL.List, self).get_queryset(*args,**kwargs)
#			queryset = queryset.prefetch_related('orders')
#			return queryset
#	class Read(SmartReadView):
#		fields = ('email','mobile','billing_name','billing_address','billing_country','order')

class OrderCRUDL(SmartCRUDL):
	model = Order
	permissions = True
	actions = ('list','read','create','delete','update',)
	
			
	
	class List(SmartListView):
		fields = ('date','status','name','mobile','address','restaurant.restaurant_name','restaurant.service_type','additional_information')
		search_fields = ('status',)
		
		
		def get_queryset(self,*args,**kwargs):
			queryset = super(OrderCRUDL.List,self).get_queryset(*args,**kwargs)
			#if super-user,show all orders
			if self.request.user.is_superuser:
				return queryset
			return queryset.filter(restaurant__user=self.request.user).order_by('created_on')
			

			 
			
#		template_name = 'orderitem_list.html'
#		def get_total_amount(self,obj):
#			total = decimal.Decimal('0.00')
#			order_items = OrderItem.objects.filter(order=self)
#			for item in order_items:
#				total += item.total
#			return obj.total
#		def get_queryset(self,*args,**kwargs):
#			queryset = super(OrderCRUDL.List,self).get_queryset(*args,**kwargs)
#			queryset=queryset.prefetch_related('orderitems')
#			return queryset
	class Read(SmartReadView):
		fields = ('date','status','customer','restaurant','is_active')
	class Update(SmartUpdateView):
		fields = ('status','is_active')


#---------------------------------------------------------------------------
class OrderItemCRUDL(SmartCRUDL):
	model = OrderItem
	permissions = True
	actions = ('create','delete','update','list','read')
	
	class List(SmartListView):
		fields = ('item.name','item.price','quantity')
		search_fields = ()
		
#		def get_order_date(self, obj):
#			import pdb;pdb.set_trace()
#			return obj.order.date

#		def get_order_mobile(self, obj):
#			return obj.order.mobile
#		def get_order_billing_name(self,obj):
#			return obj.order.billing_name
#		def get_order_billing_address(self,obj):
#			return obj.order.billing_address
#		def get_order_billing_city(self,obj):
#			return obj.order.billing_city
#		def get_order_status(self,obj):
#			return obj.order.status

	class Read(SmartReadView):
		fields = ('item.name','item.price','quantity')


class RecievedOrderCRUDL(SmartCRUDL):
	model = RecievedOrder
	actions = ('create','read','delete','list','update')
	permissions = True
	
	class Create(SmartCreateView):
		fields = ('date_added','quantity','item.name','item.')
		
	
	class List(SmartListView):
		fields = ('order_date','order_status','order_mobile','order_name','order_address','item.name','item.price','option_name','option_price','toppings_and_extras_count','quantity','order_id','order_restaurant','order_service_type','order_additional_information')
		search_fields = ('order_id',)
		
		def get_queryset(self,*args,**kwargs):
			queryset = super(RecievedOrderCRUDL.List, self).get_queryset(*args,**kwargs)
			if self.request.user.is_superuser:
				return queryset
			return queryset.filter(order__restaurant__user=self.request.user).order_by('-created_on')			
		
		def get_order_date(self,obj):
			return obj.order.date
		def get_option_name(self,obj):
			if obj.option:
				return obj.option.name
			return None 
			
		def get_toppings_and_extras_count(self,obj):
			return obj.toppings_and_extras.count()

		def get_option_price(self,obj):
			if obj.option:
				return obj.option.price
			return None
		def get_order_status(self,obj):
			return obj.order.status
#		def get_order_email(self,obj):
#			return obj.order.email
		def get_order_mobile(self,obj):
			return obj.order.mobile
		def get_order_name(self,obj):
			return obj.order.name
		def get_order_address(self,obj):
			return obj.order.address
#		def get_order_city(self,obj):
#			return obj.order.city
		def get_order_id(self,obj):
			return obj.order.id
		def get_order_restaurant(self,obj):
			return obj.order.restaurant.restaurant_name
		def get_order_service_type(self,obj):
			return obj.order.restaurant.service_type
		def get_order_additional_information(self,obj):
			return obj.order.additional_information
		
	class Update(SmartUpdateView):
		fields = ('is_active',)
		
#		def get_order_status(self,obj):
#			return obj.order.status
	
	class Read(SmartReadView):
		fields = ('order_status','order_id','order_name','order_mobile','order_address','item.name','item.price','option_name','option_price','toppings_and_extras','quantity','order_restaurant','order_service_type',)
		
		def get_order_status(self,obj):
			return obj.order.status
		def get_order_name(self,obj):
			return obj.order.name
		def get_order_mobile(self,obj):
			return obj.order.mobile
		def get_order_address(self,obj):
			return obj.order.address
		def get_option_name(self,obj):
			if obj.option:
				return obj.option.name
			return None
		def get_option_price(self,obj):
			if obj.option:
				return obj.option.price
			return None
		def get_toppings_and_extras(self,obj):
			result=[]
			for topping in obj.toppings_and_extras.all():		
				result.append(str(topping.name) + ' ' + str((topping.price))) 
			return result
		def get_order_restaurant(self,obj):
			return obj.order.restaurant.restaurant_name
		def get_order_service_type(self,obj):
			return obj.order.restaurant.service_type
		def get_order_id(self,obj):
			return obj.order.id
	
	
			
