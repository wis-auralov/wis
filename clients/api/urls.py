from django.conf.urls import url
from .views import ClientListView, ScoreUpdateAPIView

urlpatterns = [
    url(r'^clients/$', ClientListView.as_view(), name='clients_api'),
    url(r'^update_score/$', ScoreUpdateAPIView.as_view(), name='update_score_api'),
]
