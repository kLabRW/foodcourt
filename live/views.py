from restaurant_detail.models import Restaurant
from restaurant_detail.models import Category,Item
from django.db.models import Q
#from django import forms
#from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response,render
from orders import order
from orders.models import Recieved_Order,Order
from django.core import urlresolvers
from django.http import HttpResponseRedirect
#from cart.models import OrderItem
from orders.forms import PartialOrderItemForm
from orders import forms
#from orders.models import Order
#from orders import checkout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
#from django import forms
#from restaurant_detail.models import Restaurant

def create_order(request,obj):
	"""create new online_order containing each orderitem instance,save order and empty the order."""
	anon_user = User.objects.get(id=settings.ANONYMOUS_USER_ID)
	resto = Item.objects.get(pk=obj.id)
	orders = Order()
	
	checkout_form = forms.CheckoutForm(request.POST,instance=orders)
	checkout = checkout_form.save(commit=False)
	
	checkout.created_by = anon_user
	checkout.modified_by = anon_user
	checkout.restaurant = resto.owner
#	orders.restaurant = Restaurant.objects.get(pk=id)
	checkout.status = Order.SUBMITTED
	checkout.save()
	
	if checkout.pk:
		"""if the order save suceeded"""
		cart_items = order.get_order_items(request)
		for ci in cart_items:
			"""create online_order for each order_item"""
			oi = Recieved_Order()
			oi.order = checkout
			oi.quantity = ci.quantity
			oi.created_by = anon_user
			oi.modified_by = anon_user
			oi.item = ci.item
			oi.price = ci.price
			oi.save()
		order.empty_cart(request)
	return orders
#-------------------------------------------------------------------------
# views to do with the checkout page,reciept page.
def show_checkout(request,id):
	"""checkout form to collect order information"""
	if order.is_empty(request):
		cart_url = urlresolvers.reverse('order_index')
		return HttpResponseRedirect(cart_url)
	if request.method == 'POST':
		item = Item.objects.get(pk=id)
		postdata = request.POST.copy()
		form = forms.CheckoutForm(request.POST,postdata)
		if form.is_valid():
			order_created = create_order(request,item)
			order_number = order_created.id
			if order_number:
				request.session['order_number'] = order_number
			if postdata['submit'] == 'complete order':
				reciept_url = urlresolvers.reverse('checkout_reciept')
				return HttpResponseRedirect(reciept_url)
	else:
		form = forms.CheckoutForm
	context = {
		'form':form,
	}
	return render(request,'checkout/checkout.html',context)
	
def reciept(request):	
	order_number = request.session.get('order_number','')
	if order_number:
		order = Order.objects.filter(id=order_number)[0]
		order_items = Recieved_Order.objects.filter(order=order)
#		order_subtotal = order.subtotal(request)
	else:
		cart_url = urlresolvers.reverse('order_index')
		return HttpResponseRedirect(cart_url)
	context = {
		'order_number':order_number,
		'order_items':order_items,
		'order':order,
	}
	return render_to_response('checkout/reciept.html',context,context_instance=RequestContext(request))
#---------------------------------------------------------------------------------------------------------
# Returns Menu of a given restaurant by returning all its categories
def get_category(request,restaurant_id):
	categories=Category.objects.filter(owner=restaurant_id).prefetch_related('item')
	context={
		'categories':categories,
	}
	return render(request,'category.html',context)
#------------------------------------------------------------------------------------------------------
def show_order(request,id):
	item = Item.objects.get(pk=id)
	if request.method == 'POST':
		postdata = request.POST.copy()
		if postdata['submit'] == 'Remove':
			order.remove_from_order(request)
		if postdata['submit'] == 'Update':
			order.update_order(request)
		if postdata['submit'] == 'checkout':
#			checkout_url = show_checkout(request)
			return HttpResponseRedirect(urlresolvers.reverse('checkout',kwargs={'id':item.id}))
	order_items = order.get_order_items(request)
	order_subtotal = order.order_subtotal(request,item)
	total = order_subtotal + item.owner.service_fee
	
	context = {
		'order_items':order_items,
		'order_subtotal':order_subtotal,
		'item': item,
		'total': total,
	}
	return render_to_response('public/order.html',context,context_instance=RequestContext(request))

def show_item(request,id):
	# need to evaluate the HTTP method
	if request.method == 'POST':
#		import pdb;pdb.set_trace()
		a = Item.objects.get(pk=id)
		form = PartialOrderItemForm(request.POST,instance=a)
		# check validation of posted data
		if form.is_valid():
			order.add_to_order(request,a)
			 
			# if test cookie worked, get rid of it
			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()
			url =urlresolvers.reverse('order_index',kwargs={'id':a.id})
			# redirect to order page
			return HttpResponseRedirect(url)
	else:
		form = PartialOrderItemForm()
	request.session.set_test_cookie()
	context={
#		'categories':categories,
		'form':form,
#		'menu':menu,
		
	}
	return render_to_response('item.html',context,context_instance=RequestContext(request))
#-------------------------------------------------------------------------------------------------------------------------
#homepage
def homepage(request):
	context={}
	return render_to_response('public/home.html',context,context_instance=RequestContext(request))
#---------------------------------------------------------------------------------
import re
def normalize_query(query_string,findterms=re.compile(r'"([^"]+)"|(\S+)').findall,normspace=re.compile(r'\s{2,}').sub):
	"""Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']"""
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
	"""returns a query, that is a combination of Q objects. That combination aims to search keywords within a model by testing the given search fields"""
	query = None # Query to search for every search term 
	terms = normalize_query(query_string)
	for term in terms:
		or_query = None # Query to search for a given term in each field
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		if query is None:
			query = or_query
		else:
			query = query & or_query
	return query

def search(request):
	query_string = ''
	found_entries = None
	search_fields = ('delivery_territory',)
	option = request.REQUEST.get('deliveryType',None)
	if option == 'D':
		start_set = Restaurant.objects.filter(service_type='DELIVERY')
	elif option == 'P':
		start_set = Restaurant.objects.filter(service_type='PICKUP')
	else:
		if option == 'A':
			start_set=Restaurant.objects.filter(service_type='ALL')
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string= request.GET['q']
		entry_query= get_query(query_string,search_fields)
		found_entries= start_set.filter(entry_query).order_by('created_on')
	context = {
		'query_string':query_string,
		'found_entries':found_entries,
	}
	return render_to_response('public/search.html',context,context_instance=RequestContext(request))

#-----------------------------------
#class ContactForm(forms.Form):
#	name = forms.CharField(max_length=100)
#	email= forms.EmailField()
#	message = forms.CharField(widget=forms.Textarea())
	
#def contact(request):
#	if request.method == 'POST':
#		form = ContactForm(request.POST)
#		if form.valid():
#			name=form.cleaned_data['name']
#			email=form.cleaned_data['email']
#			message = form.cleaned_data['message']
#			recipients = ['f4l@gmail.com']
#			title = 'F4L contact us message from %s' % name
#			send_mail(title,message + '\n \nFrom ' + name + '\nReply to ' + email,email, recipients)
#			return render_to_response('public/contact_success.html',context_instance=RequestContext(request))
#	else:
#		form = ContactForm()
#	return render(request,'public/contact.html',{'form':form})

# Not necessary at the moment.
#def show_checkout(request):
#	if order.is_empty(request):
#		cart_url = urlresolvers.reverse('order_index')
#		return HttpResponseRedirect(cart_url)
#	if request.method == 'POST':
#		postdata = request.POST.copy()
#		form = forms.CheckoutForm(request.POST,postdata)
#		if form.is_valid():
#			response = checkout.process(request)
#			order_number = response.get('order_number',0)
#			error_message = response.get('message','')
#			if order_number:			
#				request.session['order_number'] = order_number
#			if postdata['submit'] == 'place order':
#				reciept_url = urlresolvers.reverse('checkout_reciept')
#				return HttpResponseRedirect(reciept_url)
#		else:
#			error_messages = u'Correct these errors'
#	else:
#		form = forms.CheckoutForm()
#	context = {
#		'form':form,
#		'error_message':error_message
#	}
#	return render_to_response('checkout/checkout.html',context,context_instance=RequestContext(request))
	
#def reciept(request):	
#	order_number = request.session.get('order_number','')
#	if order_number:
#		order = Order.objects.filter(id=order_number)[0]
#		order_items = OrderItem.objects.filter(order=order)
#		del request.session['order_number']
#	else:
#		order_url = urlresolvers.reverse('order_index')
#		return HttpResponseRedirect(order_url)
#	context = {
#		'order':order,
#		'order_items':order_items,
#	}
#	return render_to_response('checkout/reciept.html',context,context_instance=RequestContext(request))
#------------
