#from live.views import show_order
from .views import OrderCRUDL,OrderItemCRUDL,Recieved_OrderCRUDL
from django.conf.urls.defaults import patterns, include, url

urlpatterns = OrderCRUDL().as_urlpatterns()
urlpatterns += OrderItemCRUDL().as_urlpatterns()
urlpatterns += Recieved_OrderCRUDL().as_urlpatterns()
#urlpatterns += Recieved_ordersCRUDL().as_urlpatterns()
#urlpatterns = patterns('',
#	url(r'^$/',show_order,name='order_index'),
#)
