from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^product_list/', include('product_list.urls', namespace="product_list")),
    url(r'^admin/', include(admin.site.urls)),
)
