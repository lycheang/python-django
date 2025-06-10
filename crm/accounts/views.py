from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Account  # Make sure your Account model is imported correctly


def accounts_list(request):
    MAX_OBJECTS = 20
    accounts = Account.objects.all()[:MAX_OBJECTS]
    data = {
        "results": list(accounts.values("question", "created_by__username", "pub_date"))
    }
    return JsonResponse(data)


def accounts_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    data = {
        "results": {
            "question": account.question,
            "created_by": account.created_by.username,
            "pub_date": account.pub_date,
        }
    }
    return JsonResponse(data)
