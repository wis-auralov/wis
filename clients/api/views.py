from django.db.models import F, Case, When
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView

from rest_framework.views import APIView

from clients.models import Client


class ClientSerializer(ModelSerializer):
    read_only_fields = ('image_url',
                        'score')

    class Meta:
        model = Client
        fields = [
            'id',
            'image_url',
            'score',
        ]


class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ScoreUpdateAPIView(APIView):
    def patch(self, request, *args, **kwargs):
        client_id =request.data.get('client')
        if client_id:
            Client.objects.filter(id=client_id).update(score=Case(
                When(
                    score__lt=10, then=F('score') + 1
                ),
                default=F('score')
            ))
        return Response()