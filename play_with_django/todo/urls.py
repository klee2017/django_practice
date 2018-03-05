from django.conf.urls   import url

from . import views_fbv
from . import views_cbv

urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$', views_fbv.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views_fbv.hello),

    url(r'^list1/$', views_fbv.post_list1),
    url(r'^list2/$', views_fbv.post_list2),
    url(r'^list3/$', views_fbv.post_list3),
    url(r'^excel/$', views_fbv.excel_download),

    url(r'^cbv/list1/$', views_cbv.post_list1),
    url(r'^cbv/list2/$', views_cbv.post_list2),
    url(r'^cbv/list3/$', views_cbv.post_list3),
    # url(r'^cbv/excel/$', views_cbv.excel_download),
]