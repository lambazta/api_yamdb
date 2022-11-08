import csv

from reviews.models import User


def run():
    with open('static/data/users.csv') as file:
        reader = csv.reader(file)
        next(reader)

        # Genre.objects.all().delete()

        for row in reader:
            print(row)

            # category, _ = Genre.objects.get_or_create(id=row[3])

            user = User(
                id=row[0],
                username=row[1],
                email=row[2],
                role=row[3],
                bio=row[4],
                first_name=row[5],
                last_name=row[6],
            )
            user.save()
