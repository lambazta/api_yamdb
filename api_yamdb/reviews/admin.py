from django.contrib import admin

# from .models import Titles, Genres, Category
from .models import Title, Review, Comment


class TitlesAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'name', 'year', 'description',
                    'category', 'rating')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name',)


admin.site.register(Title, TitlesAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('id', 'title_id', 'text', 'score', 'author', 'pub_date')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)


admin.site.register(Review, ReviewsAdmin)


class CommentsAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('review_id', 'text', 'author', 'pub_date')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)


admin.site.register(Comment, CommentsAdmin)
