from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    MovieViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register("genre", GenreViewSet)
router.register("movie", MovieViewSet)
router.register("actor", ActorViewSet)
router.register("cinema_hall", CinemaHallViewSet)
router.register("movie_session", MovieSessionViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
