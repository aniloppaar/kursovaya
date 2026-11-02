from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TourViewSet, BookingViewSet, 
    DestinationViewSet, AdvantageViewSet, SiteSettingsViewSet
)

router = DefaultRouter()
router.register(r'tours', TourViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'destinations', DestinationViewSet)
router.register(r'advantages', AdvantageViewSet)
router.register(r'settings', SiteSettingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]