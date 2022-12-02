from django.contrib import admin
from django import forms
from .models import Product, Category, Review, Rating, RatingStar


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'url')
    list_display_links = ('title',)


class ReviewInLine(admin.ModelAdmin):

    model = Review
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = '__all__'
    list_filter = ('category', 'created_at', 'draft',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'parent')
    readonly_fields = ('name', 'email')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    list_display = ('star', 'product', 'ip')


admin.site.register(RatingStar)