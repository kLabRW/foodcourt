from django.conf.urls.defaults import patterns, include, url
from .views import *

activation = RestaurantCRUDL().view_for_action('activate').as_view()
#new = RestaurantCRUDL().view_for_action('new').as_view()


urlpatterns = Restaurant_detailCRUDL().as_urlpatterns()
urlpatterns += RestaurantCRUDL().as_urlpatterns()
urlpatterns += CategoryCRUDL().as_urlpatterns()
urlpatterns += ItemCRUDL().as_urlpatterns()
urlpatterns += patterns('/^restaurant_detail/', url(r'/activate/(?P<token>\w+)/$',activation, name='url_activation'),)

#urlpatterns += patterns('/^restaurant_detail/', url(r'/new/$', new, name='url_new'),)
