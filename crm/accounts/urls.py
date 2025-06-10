from django.urls import include, path
from .views import accounts_list,accounts_detail
urlpatterns = [
    path('accounts/', accounts_list, name='accounts_list'),
    path('accounts/<int:pk>/', accounts_detail, name='accounts_detail'),
    
]