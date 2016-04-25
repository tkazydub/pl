from django.conf.urls import url
from product_list import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<list_id>[0-9]+)/$', views.DetailedView, name='detail'),
    url(r'^lists/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^remove_item/(?P<item_id>\d+)/$', views.remove_item, name='remove_item'),
    url(r'^update_item/(?P<item_id>\d+)/$', views.update_item, name='update_item'),
    url(r'^edit_item/(?P<pk>\d+)/$', views.EditItemView.as_view(), name='edit_item'),
    url(r'^add_new_item/$', views.add_new_item, name="add_item"),
    url(r'^add_item_to_list/(?P<pk>\d+)/$', views.AddCustomItemView.as_view(), name="add_item_to_list"),
    url(r'^remove_item_from_list/(?P<list_id>\d+)/(?P<item_id>\d+)/$', views.remove_item_from_list, name="remove_item_from_list"),
    url(r'^desc_list_link/(?P<list_id>\d+)/(?P<item_id>\d+)/(?P<desc_id>\d+)/$', views.desc_list_link, name="desc_list_link"),
    url(r'^add_new_list/$', views.add_new_list, name="add_new_list"),
    url(r'^add_new_list/add/$', views.add_list, name="add_list"),
    url(r'^remove_list/(?P<list_id>\d+)/$', views.remove_list, name="remove_list"),
    url(r'^add_new_item/save/$', views.save_item, name='save_item'),
    url(r'^save_item_to_list/(?P<item_id>\d+)/$', views.save_item_to_list, name='save_item_to_list'),
    url(r'^desc_list/(?P<list_id>\d+)/(?P<item_id>\d+)/$', views.LinkItemDescView.as_view(), name='desc_list'),
    url(r'^items/$', views.ShowItemsView.as_view(), name='items')
]
