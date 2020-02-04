from rest_framework import serializers

from .models import Category, Diagnosis


class CategorySerializer(serializers.ModelSerializer):
    """ crude serializer for category"""
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializerReadOnly(serializers.ModelSerializer):
    """ to serialize diagnosis category """
    class Meta:
        model = Category
        fields = ('id', 'code', 'title')


class DiagnosisSerializer(serializers.ModelSerializer):
    category_detail = serializers.SerializerMethodField()

    class Meta:
        model = Diagnosis
        # fields = '__all__'
        fields = (
            'id', 'category', 'code', 'full_code', 'abbreviated_description', 'full_description',
            'backward_compatible', 'created', 'updated', 'category_detail',
        )

    def get_category_detail(self, obj):
        return CategorySerializerReadOnly(obj.category).data
