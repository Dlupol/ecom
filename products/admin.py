from django.contrib import admin
from django import forms
from .models import *


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


admin.site.register(Category)


class ReviewInLine(admin.ModelAdmin):

    model = Review
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('title', 'draft', 'created_at')
    list_filter = ('category', 'created_at', 'draft',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'parent')
    readonly_fields = ('name', 'parent', 'product')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    list_display = ('star', 'product', 'ip')


admin.site.register(RatingStar)

admin.site.register(Artist)
admin.site.register(Cart)
admin.site.register(CartItems)
