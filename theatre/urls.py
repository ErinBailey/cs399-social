from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django import views

# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'theatre.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^dreams/', 'theatre.views.dream_info', name='dreams'),
    url(r'^login/', 'theatre.views.login', name='login'),
    url(r'^flock/', 'theatre.views.flock_info', name='flock'),
    url(r'^logout/', 'theatre.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
