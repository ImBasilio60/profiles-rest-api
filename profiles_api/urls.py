from django.urls import path

#for viewSet
from django.urls import include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')


urlpatterns = [
    # APIVIEW
    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    # VIEWSET
    path('', include(router.urls))
]