from menu_category import Category
from menu_item import Item
from f4l import settings
def foodforless(request): 
	return {
		'active_categories':Category.objects.filter(is_active=True),
		'active_items':Item.objects.filter(is_active=True),
		'site_name':settings.SITE_NAME,
		'meta_keywords':settings.META_KEYWORDS,
		'meta_description':settings.META_DESCRIPTION,
		'request':request,
}
