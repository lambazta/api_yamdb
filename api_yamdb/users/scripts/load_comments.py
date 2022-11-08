import csv

from django.shortcuts import get_object_or_404
from reviews.models import Comment, Review, User


def run():
    with open('static/data/comments.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Comment.objects.all().delete()

        for row in reader:
            print(row)

            review, _ = Review.objects.get_or_create(id=row[1])
            # user, _ = User.objects.get_or_create(id=row[3])
            user = get_object_or_404(User, id=row[3])

            comment = Comment(
                id=row[0],
                review_id=review,
                text=row[2],
                author=user,
                pub_date=row[4],
            )
            comment.save()
