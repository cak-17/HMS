from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"", views.RoomViewSet)
router.register(r"category", views.RoomCategoryViewSet, basename="roomcategory") 

urlpatterns = [
    path("check_avail/", views.check_avail, name="chekc_avail"),
    path("", include(router.urls))
]
