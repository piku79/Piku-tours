"""Piku_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings


from viewer.views import (
    WelcomeView, TravelListView, TravelDetailView,
    CreateTravelView, UpdateTravelView, DeleteTravelView, ContactView, RegisterUser,
    RateTravel, FavoriteTravelsListView,
)

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('admin/', admin.site.urls),
    path('travels', TravelListView.as_view(), name='travels'),
    path('travels/favorites', FavoriteTravelsListView.as_view(), name='favorite_travels'),
    path('travels/<int:pk>', TravelDetailView.as_view(), name='travel_details'),
    path('travels/create', CreateTravelView.as_view(), name='create_travels'),
    path('travels/<int:pk>/update/', UpdateTravelView.as_view(), name='update_travels'),
    path('travels/<int:pk>/delete/', DeleteTravelView.as_view(), name='delete_travels'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact', ContactView.as_view(), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('travels/<int:pk>/rate/', RateTravel.as_view(), name='rate_travel'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
