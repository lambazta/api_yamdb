from rest_framework import serializers
from users.models import User
from reviews.models import Category, Genre, Title
from reviews.models import Review, Comment


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class VerifyAccountSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role')


class MeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role')
        read_only_fields = ('role',)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )
    rating = serializers.IntegerField(
        source='reviews__score__avg', read_only=True
    )

    class Meta:
        model = Title
        fields = '__all__'


class ReadOnlyTitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField(
        source='reviews__score__avg', read_only=True
    )

    class Meta:
        model = Title
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    # title = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Review
        fields = ('title_id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('title_id', 'author',)

    def validate_score(self, score):
        if not (0 < score <= 10):
            raise serializers.ValidationError(
                'Рейтинг должен быть в интервале от 1 до 10.'
            )
        return score

    def validate(self, data):
        request = self.context.get('request')
        title_id = self.context.get('view').kwargs.get('title_id')
        if (
            Review.objects.filter(title_id=title_id,
                                  author=request.user).exists()
            and request.action == 'create'
        ):
            raise serializers.ValidationError(
                'Вы можете оставить только один отзыв!'
            )
        return data


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('review_id', 'text', 'author', 'pub_date')
        read_only_fields = ('riview_id', 'author',)
