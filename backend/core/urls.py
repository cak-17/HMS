from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"hotel", views.HotelViewSet)
router.register(r"services", views.ServiceViewSet)
router.register(r"guests", views.GuestViewSet)
urlpatterns = [
    path("", include(router.urls))
]
