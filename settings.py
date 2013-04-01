# Django settings for a generic project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
	('mark musasizi', 'food4lessrwanda@gmail.com') 
)
SEND_BROKEN_LINK_EMAILS = True

MANAGERS = ADMINS

## Pull in CloudFoundry's production settings
if 'VCAP_SERVICES' in os.environ:
    import json
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])
    # XXX: avoid hardcoding here
    mysql_srv = vcap_services['mysql-5.1'][0]
    cred = mysql_srv['credentials']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': cred['name'],
            'USER': cred['user'],
            'PASSWORD': cred['password'],
            'HOST': cred['hostname'],
            'PORT': cred['port'],
            }
        }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "dev.db",
            "USER": "",
            "PASSWORD": "",
            "HOST": "",
            "PORT": "",
            }
        }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''
DATE_FORMAT = "d-m-Y"
DATETIME_FORMAT = "d-m-Y H:i"
SITE_NAME = 'Food for less'
META_KEYWORDS = 'Food,order,online,delivery,pickup,service,restaurant,kigali,Rwanda'
META_DESCRIPTION = "Food for less is an online food ordering, delivery and pickup service from kigali,Rwandas' finest restaurants."
RATINGS_VOTES_PER_IP = 3 #to limit the number of unique IPs per object/rating-field combination. 

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
ROOT_PATH = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(ROOT_PATH, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
#	"/home/matsinvasion/food4less/static/css"
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0tc6gk^8x=lfzyh0&amp;%1u^7tu0wb(aho7o6+6!*yr!=#c#b4c$@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'marketing.urlcanon.URLCanonicalizationMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROUTER_PASSWORD = "test"

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # added packages,
    'guardian',
    #nyaruka packages,
    'smartmin',
    'django_quickblocks',
    'rapidsms',
    'rapidsms_httprouter',
    'nsms',
    'nsms.console',
    #project apps and packages
    'echo',
    'django_extensions',
    'sorl.thumbnail',
    'pagination',
    'djangoratings',
    'agon_ratings',
    'restaurant_detail',
    'live',
    'debug_toolbar',
    'orders',
    # marketing
    
    
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)
#------------------------------
THUMBNAIL_DEBUG = True
#CACHE_BACKEND = 'memcached://127.0.0.1:8000/'
THUMBNAIL_CACHE_TIMEOUT= 3600 * 24 * 365
#----------------------------------------------------
AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'guardian.backends.ObjectPermissionBackend',
)
#Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'food4lessrwanda@gmail.com'
EMAIL_HOST_PASSWORD = 'timewilltell81'
EMAIL_USE_TLS = True

#LOGIN DETAILS
LOGIN_URL = "/users/login"
LOGOUT_URL = "/users/logout/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
# this is needed by guardian
ANONYMOUS_USER_ID = -1

# create the smartmin CRUDL permissions on all objects
PERMISSIONS = {
  '*': ('create', # can create an object
        'read',   # can read an object, viewing it's details
        'update', # can update an object
        'delete', # can delete an object,
        'list'),  # can view a list of the objects
  'restaurant_detail.restaurant':('myprofile','new','item','category',),
 
 
}
GROUP_PERMISSIONS = {
    "Administrator": ('auth.user.*','restaurant_detail.restaurant_detail.*','restaurant_detail.restaurant_read','orders.order.*','orders.orderItem.*','orders.orderitem.*','orders.orderitem_list','orders.order.*','orders.recieved_order.*','django_quickblocks.quickblocks.*','django_quickblocks.quickblocktype.*',),
    "Restaurants": ('restaurant_detail.restaurant_myprofile','restaurant_detail.restaurant_read','restaurant_detail.item.*','restaurant_detail.category.*',),
}


RAPIDSMS_TABS = ()
SMS_APPS = ['echo']
DEFAULT_BACKEND = "console"
DEFAULT_COUNTRY_CODE = "250"

#cookie name. This can be whatever we want
SESSION_COOKIE_NAME = 'sessionid'
#The module to store sessions data.
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
#Age of cookie, in seconds(default: 2 weeks).
SESION_COOKIE_AGE = 60 * 60 *24 * 7 * 2
#whetehr a user's session expires when they close the web browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
#whether the session cookie should be secure(https:// only)
SESSION_COOKIE_SECURE = False

CACHES = {
	'default':{
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': '127.0.0.1:11211'
	}
}

DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS':False
}

INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)


INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }
