#order processing

#from .models import Customer
#from orders import forms
#from f4l import settings
from django.core import urlresolvers
#from orders import order
#from .authnet import do_auth_capture
#import urllib
#from django.conf import settings
from django.contrib.auth.models import User


# returns the URL from the checkout module for order
def get_checkout_url(request,restaurant_id):
	resto = Order.objects.get(restaurant = restaurant_id)
	return urlresolvers.reverse('checkout',args=(resto))
#will be called by views after form validation


#def save_checkout_details(request):
#	anon_user = User.objects.get(id = settings.ANONYMOUS_USER_ID)
#	details = Customer(created_by = anon_user,modified_by=anon_user)
#	details.save()













#def process(request):
#	""" takes a POST request containing valid order data; pings the payment gateway with the billing 
 #   information and returns a Python dictionary with two entries: 'order_number' and 'message' based on
#    the success of the payment processing. An unsuccessful billing will have an order_number of 0 and an error message, 
 #   and a successful billing with have an order number and an empty string message.
    
 #   """
	#Transaction results
#	APPROVED = '1'
#	DECLINED = '2'
#	ERROR = '3'
#	HELD_FOR_REVIEW = '4'
#	postdata = request.POST.copy()
#	card_num = postdata.get('credit_card_number','')
#	exp_month = postdata.get('credit_card_expire_month','')
#	exp_year = postdata.get('credit_card_expire_year','')
#	exp_date = exp_month + exp_year
#	cvv = postdata.get('credit_card_cvv','')
#	amount = order.order_subtotal(request)
#	results = {}
#	response = do_auth_capture(amount=amount,
#	card_num=card_num,exp_date=exp_date,card_cvv=cvv,)
#	if response[0] == APPROVED:
#		transaction_id = response[6]
#		orders = create_order(request,transaction_id)
#		results = {'order_number':order_id,'message':''}

#	if response[0] == DECLINED:
#		results = {'order_number':0,'message':'Dear Customer,there is a problem with your credit_card.'}
#	if response[0] == ERROR or response[0] == HELD_FOR_REVIEW:
#		results = {'order_number':0,'message':'Dear customer,Error Processing your order.'}
#	return results
	
#def create_order(request):
#	""" if the POST to the payment gateway successfully billed the customer, create a new order
 #   containing each CartItem instance, save the order with the transaction ID from the gateway,
  #  and empty the shopping cart
    
   # """
#	orderz = Order()
#	checkout_form = forms.CheckoutForm(request.POST, instance=orderz)
#	anon_user = User.objects.get(id=settings.ANONYMOUS_USER_ID)
#	orderz = checkout_form.save(commit=False)
#	order.transaction_id = transaction_id
#	orderz.status = Order.SUBMITTED
#	orderz.created_by = anon_user
#	orderz.modified_by = anon_user
##	""" if order save succeeded"""
#	if orderz.pk:
#		order_items = order.get_order_items(request)
#		for ci in order_items:
#			try:
#				food_order = Order.objects.get(pk=order_id)
#				restaurant = Restaurant.objects.get(pk=restaurant_id)
#			except: 
#				food_order = Order(created_by=anon_user,modified_by=anon_user)
#				food_order.save()
#			""" create order item for each cart item"""
#			oi = OrderItem()
#			oi.created_by = anon_user
#			oi.modified_by = anon_user
#			oi.order = food_order
#			oi.orders = order
#			oi.quantity = ci.quantity
#			oi.item = ci.item
#			oi.save()
		#all set,empty cart
#		order.empty_cart(request)
	#return new order object
#	return order 
			
	
	
