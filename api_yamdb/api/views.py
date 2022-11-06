from rest_framework import viewsets
from reviews.models import Review, Title, Comment
# from users.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from .permissions import AuthorizedOrReadOnly
from .serializers import CommentsSerializer, ReviewsSerializer
from rest_framework.pagination import LimitOffsetPagination


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    permission_classes = [AuthorizedOrReadOnly]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return get_list_or_404(Review, title_id=self.kwargs.get('title_id'))

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [AuthorizedOrReadOnly]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return get_list_or_404(Comment, review_id=self.kwargs.get('review_id'))

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
