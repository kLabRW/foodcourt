# Create your views here.
from .models import *
from smartmin.views import *
from .models import RestaurantDetail,Restaurant,Item,Category
from django.conf import settings
from django.contrib.auth.models import User, Group
from orders import models
import random
import string
from django import forms
# copying user views from smartmin views...did some editting
class RestaurantForm(forms.ModelForm):
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput)


    def save(self, commit=True):
        """
        Overloaded so we can save any new password that is included.
        """
        restaurant = super(RestaurantForm, self).save(commit)
        new_pass = self.cleaned_data['new_password']
        # new passwords should be made active by default
        if new_pass:
			restaurant.user.set_password(new_pass)
			restaurant.is_active=True
			restaurant.user.save()
			if (commit):
				restaurant.save()
	return restaurant

    class Meta:
        model = Restaurant
        fields = ('is_active','restaurant_name','first_name','last_name','mobile','cusine', 'service_type','service_days','service_hours_start','service_hours_end','minimum_order_amount','delivery_territory','token','restaurant_name','logo','cusine','closed',)


#----------------------------------------------------------------
class RestaurantDetailCRUDL(SmartCRUDL):
	model = RestaurantDetail
	actions = ('create', 'read','list','update','thanks',)
	permissions = True
	
   	class List(SmartListView):
		fields = ('restaurant_name','first_name','last_name','mobile','cusine', 'service_type','service_fee','service_days','service_hours_start','service_hours_end','minimum_order_amount','delivery_territory','closed')
		search_fields =('restaurant_name__icontains','cusine__icontains',)
		field_config = {'services': dict(label = "SERVICES")}
		
		def derive_queryset(self, **kwargs):
			queryset = super(Restaurant_detailCRUDL.List, self).derive_queryset(**kwargs)
			return queryset.filter(is_active=True)
		
		def get_name(self, obj):	
			return "%s" % (obj.restaurant_name)
#		def get_service_days(self,obj):
#			return obj.get_service_days_display()
#		def get_delivery_hours_start(self,obj):
#			return get_delivery_hours_start_display()
#		def get_delivery_hours_end(self,obj):
#			return get_delivery_hours_end_display()
#		def get_pickup_days(self,obj):
#			return obj.get_pickup_days_display()
#		def get_pickup_hours_start(self,obj):
#			return get_pickup_hours_start_display()
#		def get_pickup_hours_end(self,obj):
#			return get_pickup_hours_end_display()
		
	class Read(SmartReadView):
		fields= ('restaurant_name','first_name','last_name','mobile','email','cusine','logo','address','service_type','delivery_fee','approve','service_hours_start','service_hours_end','service_days','minimum_order_amount','delivery_territory','closed')
		def get_approve(self,obj):
			restaurant=Restaurant.objects.filter(restaurant_detail=obj)
			if restaurant:
				return '<a class="btn btn-large btn-success disabled" href="#"> Approved <i class="icon=ok icon-white"></i></a>'
			else:
				return '<a class="btn btn-large posterize" href="%s?restaurant_detail=%d">Approve</a>' % (reverse('restaurant_detail.restaurant_new'), obj.id)
		def get_name(self,obj):
			return str(obj)
		
#		def get_service_days(self,obj):
#x			return obj.get_service_days_display()
		
#		def get_delivery_days(self,obj):
#			return obj.get_delivery_days_display()
	class Update(SmartUpdateView):
		fields=('restaurant_name','first_name','last_name','logo','mobile','cusine', 'service_type','service_fee','service_days','service_hours_start','service_hours_end','minimum_order_amount','closed','delivery_territory','is_active',)
	class Create(SmartCreateView):
		permission=None
		submit_button_name="Join the F4L restaurant network"
#		success_url = '/'
		success_url='id@restaurant_detail.restaurant_detail_thanks'
		
		def pre_save(self,obj):
			obj = super(Restaurant_detailCRUDL.Create,self).pre_save(obj)
			anon_user=User.objects.get(id=settings.ANONYMOUS_USER_ID)
			obj.created_by=anon_user
			obj.modified_by=anon_user
			obj.save()
			return obj
		def post_save(self,obj):
			obj=super(Restaurant_detailCRUDL.Create, self).post_save(obj)
			anon_user=User.objects.get(id=settings.ANONYMOUS_USER_ID)
			obj.created_by=anon_user
			obj.modified_by=anon_user
			obj.save()
			return obj
			
			#make any application with the same email inactive
			Restaurant_detail.objects.filter(is_active=True, email=obj.email).exclude(id=obj.id).update(is_active=False)
			return obj
		def form_valid(self,form):
			#is our hidden field displayed? we are probably a bot, return 200 request
			if 'message' in self.request.REQUEST and len(self.request.REQUEST['message'])>0: 
				return HttpResponse("Thanks for your application. You appear to be slightly automated however so we may not actually use it. If you think you have received this in error, please contact the F4L team")
			else:
				return super(Restaurant_detailCRUDL.Create, self).form_valid(form)
	class Thanks(SmartReadView):
		permission=None
#		success_url='/'
        
#--------------------------------------------------------------
class RestaurantCRUDL(SmartCRUDL):
	model= Restaurant
	actions = ('create','read','list','new','myprofile','activate')
	permissions = True
	
	class Activate(SmartUpdateView):
		form_class = RestaurantForm
		permission  = None
		success_message= "Password saved and account activated successfully, now you can login to the website"
		success_url = "@users.user_login"
		
		def derive_fields(self):
			return ('new_password',)
		def get_object(self, queryset=None):
			token=self.kwargs.get('token')
			return Restaurant.objects.get(token=token)
	class Myprofile(SmartUpdateView):
		fields=('restaurant_name','first_name','last_name','address','logo','mobile','cusine', 'service_type','service_fee','service_days','service_hours_start','service_hours_end','minimum_order_amount','closed','delivery_territory','is_active')
		def has_permission(self, request, *args, **kwargs):
			super(RestaurantCRUDL.Myprofile,self).has_permission(request,*args,**kwargs)
			return True
		def get_object(self, queryset=None):
			return Restaurant.objects.get(user=self.request.user)
	class Read(SmartReadView):
		fields = ('restaurant_name','first_name','last_name','mobile','email','cusine','logo','address', 'service_type','service_days','service_hours_start','service_hours_end','minimum_order_amount','closed','delivery_territory')
	class List(SmartListView):
		fields =('restaurant_name,first_name','last_name','mobile','email','address')
		field_config={'email':dict(label="Email/User")}
		def derive_queryset(self,**kwargs): 
			queryset= super(RestaurantCRUDL.List, self).derive_queryset(**kwargs)
			return queryset.filter(is_active=True)
		def get_name(self, obj):
			return "%s %s " % (obj.first_name, obj.last_name)
		
	class New(SmartCreateView):
		fields=('restaurant_detail',)
		success_url='id@restaurant_detail.restaurant_read'
			
		def pre_save(self,obj):
			obj=super(RestaurantCRUDL.New, self).pre_save(obj)
			userapp=obj.restaurant_detail
			obj.first_name=userapp.first_name
			obj.last_name=userapp.last_name
			obj.restaurant_name=userapp.restaurant_name
			obj.address=userapp.address
			obj.mobile=userapp.mobile
			obj.email=userapp.email
			obj.logo=userapp.logo
			obj.cusine=userapp.cusine
			obj.service_type=userapp.service_type
			obj.service_fee=userapp.service_fee
			obj.service_days=userapp.service_days
			obj.service_hours_start=userapp.service_hours_start
			obj.service_hours_end=userapp.service_hours_end
			obj.minimum_order_amount=userapp.minimum_order_amount
			obj.closed = userapp.closed
			obj.delivery_territory=userapp.delivery_territory
			obj.token=''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
				
			user=User.objects.create(username=obj.restaurant_detail.email,email=obj.restaurant_detail.email)
			user.email_user("F4L account activation","Your membership to F4L has been approved go to the following link to activate your account \n \n http://f4l.herokuapp.com/restaurant_detail/restaurant/activate/%s/ \n \n After you have activated your account, login using your full email address as username and your password \n \n And customize what will be published on your F4L website profile by click profile link on the left of members \n \n This email is generated by the F4L website do not reply to it. " % obj.token,"website@f4l.herokuapp.com")
			group=Group.objects.get(name='Restaurants')
			user.first_name=userapp.first_name
			user.last_name=userapp.last_name
			user.email=userapp.email
			user.set_unusable_password()
			user.save()
			user.groups.add(group)
				
			obj.user=user
			obj.is_active=False
			obj.save()
			return obj			
		def post_save(self,obj):
			obj=super(RestaurantCRUDL.New, self).post_save(obj)
			obj.update_restaurant_logo()
			obj.save()
			return obj
		
#----------------------------------------------------------------------------
# Create your views here.
#overidin and create custom form, thanks to nick and eric.
class CategoryCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs['user']
		#delete user because with super it will blow up
		del kwargs['user']
		super(CategoryCreateForm, self).__init__(*args, **kwargs)
		#query on field, item created by user.
		self.fields['item'].queryset = Item.objects.filter(created_by=user)
	
	class Meta:
		model = Category

class CategoryUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs['user']
		#delete user because with super it will blow up
		del kwargs['user']
		super(CategoryUpdateForm, self).__init__(*args, **kwargs)
		#query on field, item created by user.
		self.fields['item'].queryset = Item.objects.filter(created_by=user)
#		self.fields['owner'].queryset = Item.objects.filter(owner=user)
	
	class Meta:
		model = Category
	

class CategoryCRUDL(SmartCRUDL):
	model = Category
	permissions = True
	fields = ('create','read','update','list','shortlist')
	
	class Create(SmartCreateView):
		fields = ('title','item','display_order')
		form_class = CategoryCreateForm
		
#		def get_item_name(self,obj):
#			return obj.item.name
		
		def get_form_kwargs(self):
			kwargs = super(CategoryCRUDL.Create, self).get_form_kwargs()
			kwargs['user'] = self.request.user
			return kwargs
		
		def pre_save(self,obj):
			obj = super(CategoryCRUDL.Create,self).pre_save(obj)
			restaurant = Restaurant.objects.get(user=self.request.user)
			obj.owner = restaurant
			return obj
	
	class Read(SmartReadView):
		
		fields=('title','item','display_order')
		
		def get_title(self,obj):
			return str(obj)
				
	class List(SmartListView):
		fields = ('title',)
		
		def derive_queryset(self):
			restaurant = Restaurant.objects.get(user=self.request.user)
			return Category.objects.filter(owner=restaurant)
	class Update(SmartUpdateView):
		fields = ('item','title','is_active','display_order')
		form_class = CategoryUpdateForm
		
		def get_form_kwargs(self):
			kwargs = super(CategoryCRUDL.Update,self).get_form_kwargs()
			kwargs['user'] = self.request.user
			return kwargs
		
		def derive_queryset(self):
			restaurant = Restaurant.objects.get(user=self.request.user)
			return Category.objects.filter(owner=restaurant)


#-------------------------------------------------------------------------

#overidin and create custom form, thanks to nick and eric.
class ItemCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs['user']
		#delete user because with super it will blow up
		del kwargs['user']
		super(ItemCreateForm, self).__init__(*args, **kwargs)
		#query on field, item created by user.
		self.fields['subcategory'].queryset = models.SubCategory.objects.filter(created_by=user)
	
	class Meta:
		model = Item

class ItemUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs['user']
		#delete user because with super it will blow up
		del kwargs['user']
		super(ItemUpdateForm, self).__init__(*args, **kwargs)
		#query on field, item created by user.
		self.fields['subcategory'].queryset = models.SubCategory.objects.filter(created_by=user)
#		self.fields['owner'].queryset = Item.objects.filter(owner=user)
	
	class Meta:
		model = Item
	
class ItemCRUDL(SmartCRUDL):
	model = Item
	actions = ('create','read','update','list',)
	permissions = True
#	form_class = ItemCreateForm
#	prepopulated_fields = {'slug':('name',)}


	class Create(SmartCreateView):
		fields = ('name','optionalitems','toppings_and_extras','description','price')
		
#		def get_form_kwargs(self):
#			kwargs = super(ItemCRUDL.Create, self).get_form_kwargs()
#			kwargs['user'] = self.request.user
#			return kwargs
		
		def pre_save(self,obj):
			obj = super(ItemCRUDL.Create, self).pre_save(obj)
			restaurant = Restaurant.objects.get(user=self.request.user)
			obj.owner = restaurant
			return obj
	class Read(SmartReadView):
		fields = ('name','description','price')
		
		def get_name(self,obj):
			return str(obj)
		def get_owner(self,obj):
			return str(obj.owner)
	
	class List(SmartListView):
		fields = ('name','price')
        # overiding get_queryset from smartminListView. 	
		def derive_queryset(self):
#			import pdb;pdb.set_trace()
			restaurant = Restaurant.objects.get(user=self.request.user)
			return Item.objects.filter(owner=restaurant)
	class Update(SmartUpdateView):
		fields = ('name','optionalitems','toppings_and_extras','description','price','is_active')
#		form_class = ItemUpdateForm
		
#		def get_form_kwargs(self):
#			kwargs = super(ItemCRUDL.Update,self).get_form_kwargs()
#			kwargs['user'] = self.request.user
#			return kwargs
		
		def derive_queryset(self):
			restaurant = Restaurant.objects.get(user=self.request.user)
			return Item.objects.filter(owner=restaurant)
