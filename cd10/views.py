from rest_framework import viewsets
from rest_framework.response import Response

from cd10 import serializers, models, cache_utils


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
        """ so queryset is evaluated on every request """
        return models.Diagnosis.objects.select_related('category').all()

    def get_object(self):
        # get object id
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        diag_id = self.kwargs[lookup_url_kwarg]

        c = cache_utils.DiagnosisCache(diag_id=diag_id)
        obj = c.get_data()
        if obj:
            # check obj permission
            self.check_object_permissions(self.request, obj)
            return obj

        obj = super(DiagnosisViewSet, self).get_object()
        c.set_data(obj)
        return obj

    def create(self, request, *args, **kwargs):
        # add newly created to cache
        return super(DiagnosisViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # we could update cache
        return super(DiagnosisViewSet, self).update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
        # serialized_data = serializers.serialize_diagnosis(instance)
        # return Response(serialized_data)

    def destroy(self, request, *args, **kwargs):
        # get object id
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        diag_id = self.kwargs[lookup_url_kwarg]

        # remove from cache
        c = cache_utils.DiagnosisCache(diag_id=diag_id)
        c.remove_data()

        return super(DiagnosisViewSet, self).destroy(request, *args, **kwargs)
