from .views import show_item,show_checkout,show_order,get_category,search,homepage,reciept,contact,how_it_works_page,maintence,resto_list
from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
#	url(r'^$',maintence,name="maintenance"),
	url(r'^$',homepage,name="homepage"),
	url(r'^menu/(\d+)$',get_category, name="f4l_menu"),
	url(r'^your_order/(?P<id>\d+)/$',show_order,name="order_index"),
	url(r'^item/(?P<id>\d+)/$',show_item, name="item_order"),
	url(r'^checkout/(?P<id>\d+)/$',show_checkout,name="checkout"),
	url(r'^reciept/$',reciept,name="checkout_reciept"),
	url(r'^search_results/$',search,name="search"),
	url(r'^contact/$',contact,name="contact_us"),
	url(r'^how_it_works/$',how_it_works_page,name="how_it_works"),
	url(r'^restaurants/$',resto_list,name="restaurant_list"),
#	url(r'^homepage$',homepage,name="homepage"),
#	url(r'^form/$',tryout_form,name="tryout")
 #   url(r'^search/(\d+)$',search,name="search"),
)
#urlpatterns += patterns('/^item/',url(r'^$', show_item, name = "item_order"),)
