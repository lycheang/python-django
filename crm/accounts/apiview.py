from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import Account, Choice
from .serializers import AccountSerializer


class AccountList(APIView):
    def get(self, request):
        accounts = Account.objects.all()[:20]
        data = AccountSerializer(accounts, many=True).data
        return Response(data)

class AccountDetail(APIView):
    def get(self, request, pk):
        account = get_object_or_404(Account, pk=pk)
        data = AccountSerializer(account).data
        return Response(data)