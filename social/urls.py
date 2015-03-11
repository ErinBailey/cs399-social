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

    url(r'^dreams/', 'social.views.dream_info', name='dreams'),
    url(r'^login/', 'social.views.login', name='login'),
    url(r'^flock/', 'social.views.flock_info', name='flock'),
    url(r'^about/', 'social.views.about', name='about'),
    url(r'^logout/', 'social.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
