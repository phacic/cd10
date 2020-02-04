from rest_framework import viewsets
import pprint

from cd10 import serializers, models


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.all()


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = models.Diagnosis.objects.all()
    serializer_class = serializers.DiagnosisSerializer
    page_size = 20

    def get_queryset(self):
        # return models.Diagnosis.objects.select_related('category').all()
        return models.Diagnosis.objects.select_related('category').all()

    def retrieve(self, request, *args, **kwargs):
        # diag = self.get_object()
        # pprint.pprint(diag)
        return super(DiagnosisViewSet, self).retrieve(request, *args, **kwargs)
