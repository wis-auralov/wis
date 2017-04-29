from django.conf.urls import url, include
from django.contrib import admin
from clients.views import ClientList, ClientDetail, ClientDelete, ClientCreate, ClientScores, download_xlsx

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^client_detail/(?P<pk>[0-9]+)/$', ClientDetail.as_view(), name='client_detail'),
    url(r'^client_delete/(?P<pk>[0-9]+)/$', ClientDelete.as_view(), name='client_delete'),
    url(r'^client_create/$', ClientCreate.as_view(), name='client_create'),
    url(r'^client_scores/$', ClientScores.as_view(), name='client_scores'),
    url(r'^download_file/$', download_xlsx, name='download_file'),
    url(r'^$', ClientList.as_view(), name='client_list'),
    url(r'^api/', include('clients.api.urls', namespace="api")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
