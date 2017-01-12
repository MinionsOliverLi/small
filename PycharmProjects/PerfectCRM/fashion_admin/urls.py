
from django.conf.urls import include, url
from fashion_admin import views


urlpatterns = [
    url(r'^$', views.index,name='table_index'),
    url(r'^(\w+)/(\w+)/$', views.show_table,name='show_table'),
]
