from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from djangoratings.views import AddRatingFromModel
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
#	url(r'^$', direct_to_template, {'template': 'index.html'}),
	url(r'^$',include('live.urls')),
	url(r'^users/', include('smartmin.users.urls')),
	url(r'^incoming_orders/',include('orders.urls')),
	url(r'^restaurant_detail/', include('restaurant_detail.urls')),
	url(r'^content/', include('django_quickblocks.urls')),
	url(r'rate-restaurant/(?P<object_id>\d+)/(?P<score>\d+)/', AddRatingFromModel(),{
'app_label':'restaurant_detail',
'model':'restaurant',
'field_name':'rating',
}),
	url(r'^ratings/', include("agon_ratings.urls")),
	url(r'^console/', include('nsms.console.urls')),
	url(r'^',include('rapidsms_httprouter.urls')),
	url(r'^orders/', include('live.urls')),
#	url(r'^search_results/$','f4l.views.search',),

    # Uncomment the admin/doc line below to enable admin documentation:
  #  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
 #   url(r'^admin/', include(admin.site.urls)),
)
# Static file patterns
urlpatterns += patterns('',
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	
)
