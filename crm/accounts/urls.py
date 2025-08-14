from django.urls import include, path
# from .views import accounts_list,accounts_detail
# urlpatterns = [
#     path('accounts/', accounts_list, name='accounts_list'),
#     path('accounts/<int:pk>/', accounts_detail, name='accounts_detail'),
    
# ]
# from .apiview import AccountList, AccountDetail
# urlpatterns = [
#     path('accounts/', AccountList.as_view(), name='accounts_list'),
#     path('accounts/<int:pk>/', AccountDetail.as_view(), name='accounts_detail'),
# ]
# from django.urls import path, re_path, include

# urlpatterns = [
#     re_path(r'^',include('polls.urls'))
# ]


from rest_framework.routers import DefaultRouter
from .views import AccountViewset

router = DefaultRouter()
router.register(r'accounts', AccountViewset, basename='accounts')

urlpatterns = [
    path('api/', include(router.urls)),
    

]

