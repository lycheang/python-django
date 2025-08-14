from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from .models import Account, Choice, Vote
from .serializers import AccountSerializer, ChoiceSerializer, VoteSerializer


# Custom Page Number Pagination for Account
class AccountPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'  # allows client to override
    max_page_size = 10

class CustomLimitoffPagination(LimitOffsetPagination):
    default_limit=10
    max_limit=10
class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = CustomLimitoffPagination

    # GET all accounts without pagination
    @action(detail=False, methods=['get'], url_path='all')
    def get_all_accounts(self, request):
        accounts = Account.objects.all()
        serializer = self.get_serializer(accounts, many=True)
        return Response(serializer.data)


class ChoiceViewset(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class VoteViewset(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
