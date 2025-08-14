from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


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
    
class RevokeTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"error": "Refresh token required"}, status=400)
            token = RefreshToken(refresh_token)
            token.blacklist()  # Add to blacklist
            return Response({"message": "Token revoked"})
        except Exception as e:
            return Response({"error": str(e)}, status=400)