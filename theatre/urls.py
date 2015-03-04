from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'theatre.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^dreams/', views.information_performance, name='dreams'),
    url(r'^login/', views.merchandise, name='login'),
    url(r'^flock/', views.performances, name='flock'),
    url(r'^logout/', views.ticket_sales, name='logout'),
    url(r'^bio/', views.bio, name='bio'),
    url(r'^admin/', include(admin.site.urls)),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
