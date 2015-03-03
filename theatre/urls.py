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

    url(r'^information/', views.information_performance, name='information_performance'),
    url(r'^merchandise/', views.merchandise, name='merchandise'),
    url(r'^performances/', views.performances, name='performances'),
    url(r'^ticket_sales/', views.ticket_sales, name='ticket_sales'),
    url(r'^bio/', views.bio, name='bio'),
    url(r'^admin/', include(admin.site.urls)),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
