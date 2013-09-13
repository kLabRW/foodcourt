from django.conf.urls.defaults import patterns, include, url
from .views import *
from optionalitems.views import OptionalItemCategoryCRUDL,OptionalItemCRUDL,ToppingsAndExtrasCategoryCRUDL,ToppingsAndExtraCRUDL

activation = RestaurantCRUDL().view_for_action('activate').as_view()
#new = RestaurantCRUDL().view_for_action('new').as_view()


urlpatterns = RestaurantDetailCRUDL().as_urlpatterns()
urlpatterns += RestaurantCRUDL().as_urlpatterns()
urlpatterns += CategoryCRUDL().as_urlpatterns()
urlpatterns += ItemCRUDL().as_urlpatterns()
urlpatterns += OptionalItemCategoryCRUDL().as_urlpatterns()
urlpatterns += OptionalItemCRUDL().as_urlpatterns()
urlpatterns += ToppingsAndExtrasCategoryCRUDL().as_urlpatterns()
urlpatterns += ToppingsAndExtraCRUDL().as_urlpatterns()
urlpatterns += patterns('/^restaurant_detail/', url(r'/activate/(?P<token>\w+)/$',activation, name='url_activation'),)
 

#urlpatterns += patterns('/^restaurant_detail/', url(r'/new/$', new, name='url_new'),)
