from reviews.models import Review, Title, User
from django.shortcuts import get_object_or_404
import csv


def run():
    with open('static/data/review.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Review.objects.all().delete()

        for row in reader:
            print(row)

            title, _ = Title.objects.get_or_create(id=row[1])
            # user, _ = User.objects.get_or_create(id=row[3])
            user = get_object_or_404(User, id=row[3])

            review = Review(
                id=row[0],
                title_id=title,
                text=row[2],
                author=user,
                score=row[4],
                pub_date=row[5],
            )
            review.save()
