# Create your views here.
from .models import *
from smartmin.views import *

class OptionalItemCRUDL(SmartCRUDL):
	model = OptionalItem
	actions = ('create','list','read','update',)
	permissions = True
	
	class Create(SmartCreateView):
		fields = ('name','price','description',)
		
		def pre_save(self,obj):
			obj = super(OptionalItemCRUDL.Create, self).pre_save(obj)
			restaurant = Restaurant.objects.get(user=self.request.user)
			obj.owner = restaurant
			return obj
	
	class Update(SmartUpdateView):
		fields = ('name','price','description','is_active')
		
	
	class List(SmartListView):
		fields=('name','description',)
		
	class Read(SmartReadView):
		fields = ('name','price','description')
class OptionalItemCategoryCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs['user']
		#delete user because with super it will blow up
		del kwargs['user']
		super(OptionalItemCategoryCreateForm, self).__init__(*args, **kwargs)
		#query on field, item created by user.
		self.fields['optional_items'].queryset = OptionalItem.objects.filter(created_by=user)
	
	class Meta:
		model = OptionalItemCategory

class OptionalItemCategoryUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs['user']
		#delete user because with super it will blow up
		del kwargs['user']
		super(OptionalItemCategoryUpdateForm, self).__init__(*args, **kwargs)
		#query on field, item created by user.
		self.fields['optional_items'].queryset = OptionalItem.objects.filter(created_by=user)
#		self.fields['owner'].queryset = Item.objects.filter(owner=user)
	
	class Meta:
		model = OptionalItemCategory
		
class OptionalItemCategoryCRUDL(SmartCRUDL):
	model = OptionalItemCategory
	actions = ('create','update','read','list',)
	permissions = True
	
	class Create(SmartCreateView):
		fields = ('title','optional_items','display_order',)
		form_class = OptionalItemCategoryCreateForm
		
		def get_form_kwargs(self):
			kwargs = super(OptionalItemCategoryCRUDL.Create, self).get_form_kwargs()
			kwargs['user'] = self.request.user
			return kwargs
		
		def pre_save(self,obj):
			obj = super(OptionalItemCategoryCRUDL.Create, self).pre_save(obj)
			restaurant = Restaurant.objects.get(user=self.request.user)
			obj.owner = restaurant
			return obj
		
	class Update(SmartUpdateView):
		fields = ('title','optional_items','display_order','is_active')
		form_class = OptionalItemCategoryUpdateForm
		
		def get_form_kwargs(self):
			kwargs = super(OptionalItemCategoryCRUDL.Update, self).get_form_kwargs()
			kwargs['user'] = self.request.user
			return kwargs
		
		def pre_save(self,obj):
			obj = super(OptionalItemCategoryCRUDL.Update, self).pre_save(obj)
			restaurant = Restaurant.objects.get(user=self.request.user)
			obj.owner = restaurant
			return obj 
			
	class List(SmartListView):
		fields = ('title','display_order',)
		
		
class ToppingsAndExtrasCategoryCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs['user']
		#delete user because with super it will blow up
		del kwargs['user']
		super(ToppingsAndExtrasCategoryCreateForm, self).__init__(*args, **kwargs)
		#query on field, item created by user.
		self.fields['toppings_and_extras'].queryset = ToppingsAndExtra.objects.filter(created_by=user)
	
	class Meta:
		model = ToppingsAndExtrasCategory

class ToppingsAndExtrasCategoryUpdateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs['user']
		#delete user because with super it will blow up
		del kwargs['user']
		super(ToppingsAndExtrasCategoryUpdateForm, self).__init__(*args, **kwargs)
		#query on field, item created by user.
		self.fields['toppings_and_extras'].queryset = ToppingsAndExtra.objects.filter(created_by=user)
#		self.fields['owner'].queryset = Item.objects.filter(owner=user)
	
	class Meta:
		model = ToppingsAndExtrasCategory
		
class ToppingsAndExtrasCategoryCRUDL(SmartCRUDL):
	model = ToppingsAndExtrasCategory
	actions = ('create','update','read','list',)
	permissions = True
	
	class Create(SmartCreateView):
		fields = ('title','toppings_and_extras','display_order',)
		form_class = ToppingsAndExtrasCategoryCreateForm
		
		def get_form_kwargs(self):
			kwargs = super(ToppingsAndExtrasCategoryCRUDL.Create, self).get_form_kwargs()
			kwargs['user'] = self.request.user
			return kwargs
		
		def pre_save(self,obj):
			obj = super(ToppingsAndExtrasCategoryCRUDL.Create, self).pre_save(obj)
			restaurant = Restaurant.objects.get(user=self.request.user)
			obj.owner = restaurant
			return obj
		
	class Update(SmartUpdateView):
		fields = ('title','toppings_and_extras','display_order',)
		form_class = ToppingsAndExtrasCategoryUpdateForm
		
		def get_form_kwargs(self):
			kwargs = super(ToppingsAndExtrasCategoryCRUDL.Update, self).get_form_kwargs()
			kwargs['user'] = self.request.user
			return kwargs
		
		def pre_save(self,obj):
			obj = super(ToppingsAndExtrasCategoryCRUDL.Update, self).pre_save(obj)
			restaurant = Restaurant.objects.get(user=self.request.user)
			obj.owner = restaurant
			return obj 
			
	class List(SmartListView):
		fields = ('title','display_order',)

class ToppingsAndExtraCRUDL(SmartCRUDL):
	actions = ('create','update','list','read',)
	model = ToppingsAndExtra
	permissions = True
	
	class Create(SmartCreateView):
		fields = ('name','price','description')
		
		def pre_save(self,obj):
			obj = super(ToppingsAndExtraCRUDL.Create, self).pre_save(obj)
			restaurant = Restaurant.objects.get(user=self.request.user)
			obj.owner = restaurant
			return obj
		
	class List(SmartListView):
		fields = ('name','price',)
	class Update(SmartUpdateView):
		fields = ('name','price','description')
	class Read(SmartReadView):
		fields = ('name','price','description')
	
