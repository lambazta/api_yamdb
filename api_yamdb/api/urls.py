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
from rest_framework import routers
from api.views import ReviewsViewSet, CommentsViewSet
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewsViewSet,
                basename='review')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet, basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/', include('djoser.urls')),
    # path('v1/', include('djoser.urls.jwt')),
]
