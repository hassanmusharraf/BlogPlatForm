from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from users.views import *

router = DefaultRouter()
router.register(r"blogpost", BlogPostViews)
router.register(r"tag", TagView)
router.register(r"comments", CommentsView)
router.register(r"category", CategoryView)

urlpatterns = [
    path("", include(router.urls)),
]
