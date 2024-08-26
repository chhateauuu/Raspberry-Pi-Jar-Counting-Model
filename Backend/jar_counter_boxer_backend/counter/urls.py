from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JarCountViewSet, ShiftTimingViewSet, update_jar_count

router = DefaultRouter()
router.register(r'jarcounts', JarCountViewSet)
router.register(r'shift-timings', ShiftTimingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('new_update_jar_count/', update_jar_count, name='update_jar_count'),
]
