from rest_framework import serializers
from .models import Product, Review, Rating, RatingStar, Cart, CartItems, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FilterReviewListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ProductListSerializers(serializers.ModelSerializer):

    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'image', 'price', 'rating_user', 'middle_star')


class ReviewCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):

    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ('text', 'name', 'children')


class ProductDetailSerializers(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field='category_name', read_only=True)
    reviews = ReviewSerializers(many=True)

    class Meta:
        model = Product
        exclude = ('draft', 'created_at', 'updated_at', 'in_stock')


class CreateRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('star', 'product')

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            product=validated_data.get('product', None),
            defaults={'star': validated_data.get('star')}
        )
        return rating


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemsSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = ProductDetailSerializers()

    class Meta:
        model = CartItems
        fields = '__all__'