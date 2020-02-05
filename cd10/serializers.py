import rapidjson

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
    # include category object
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


def serialize_diagnosis(diag: Diagnosis) -> dict:
    if not diag:
        return {}

    return {
        'id': diag.id,
        'category': diag.category_id,
        'code': diag.code,
        'full_code': diag.full_code,
        'abbreviated_description': diag.abbreviated_description,
        'full_description': diag.full_description,
        'backward_compatible': diag.backward_compatible,
        'created': diag.created.isoformat(),
        'updated': diag.updated.isoformat(),
        'category_detail': {
            "id": diag.category_id,
            "code": diag.category.code,
            "title": diag.category.title,
        }
    }
