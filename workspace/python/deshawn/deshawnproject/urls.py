from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from deshawnapi.views import WalkerView, CityView, DogView, AppointmentView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'walkers', WalkerView, 'walk')
router.register(r'cities', CityView, 'city')
router.register(r'dogs', DogView, 'dog')
#1st argument: URL path
#2nd argument: view that will handle client requests to that route
#3rd argument: needed for route to be registered, but it unused
router.register(r'appointments', AppointmentView, 'appointment')

urlpatterns = [
    path('', include(router.urls)),
]

