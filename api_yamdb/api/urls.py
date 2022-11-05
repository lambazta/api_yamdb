from django.urls import include, path
from rest_framework import routers
from users.views import RegistrationAPI, VerifyAccountAPI

# from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'


router_v1 = routers.DefaultRouter()
# router_v1.register(r'posts', PostViewSet)
# router_v1.register(r'groups', GroupViewSet)
# router_v1.register(r'follow', FollowViewSet, basename='follows')
# router_v1.register(
#     r'posts/(?P<post_id>\d+)/comments',
#     CommentViewSet,
#     basename='comments'
# )

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', RegistrationAPI.as_view(), name='signup'),
    path('v1/auth/token/', VerifyAccountAPI.as_view(), name='token'),
]
