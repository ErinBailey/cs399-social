from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django import views

# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'social.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/', 'social.views.about', name='about'),

    url(r'^dreams/', 'social.views.dream_info', name='dreams'),
   # url(r'^login/', 'social.views.login', name='login'),
    url(r'^flock/', 'social.views.flock_info', name='flock'),
    #url(r'^logout/', 'social.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'social.views.register', name='register'),
	url(r'^social/register/$', 'social.views.register', name='register'),


    #user auth urls
    url(r'^login/$', 'social.views.login', name='login'),
	url(r'^login/auth/$', 'social.views.login', name='login'),
    url(r'^auth/$', 'social.views.auth_view', name='auth_view'),
    url(r'^logout/$', 'social.views.logout', name='logout'),
    url(r'^loggedin/$', 'social.views.loggedin', name='loggedin'),
    url(r'^invalid/$', 'social.views.invalid_login', 'invalid_login'),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




