from django.urls import include, path
from rest_framework import routers
from .views import (
    RegistrationAPI, VerifyAccountAPI, MeViewSet, UserViewSet)

# from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'


router_v1 = routers.DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/users/me/', MeViewSet.as_view(
        {'patch': 'me',
         'get': 'me'}), name="me_viewset"),
    path('v1/auth/signup/', RegistrationAPI.as_view(), name='signup'),
    path('v1/auth/token/', VerifyAccountAPI.as_view(), name='token'),
    path('v1/', include(router_v1.urls)),
]
