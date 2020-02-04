from django.urls import path, include
from rest_framework import routers

from cd10 import views

# namespace
app_name = 'cd10'

router = routers.DefaultRouter()
router.register(r'diagnosis', viewset=views.DiagnosisViewSet)
router.register(r'categories', viewset=views.CategoryViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
