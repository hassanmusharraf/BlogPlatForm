from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from users.views import UserProfileView

router = DefaultRouter()
router.register(r"userview", UserView)
router.register(r"userprofile", UserProfileView)

urlpatterns = [path("", include(router.urls))]
