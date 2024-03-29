"""django_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from ironman.views import (
    index,
    hello,
    form,
    people_data,
    people_list,
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
    PeopleUpdateAPIView,
)
from ironman.views import (
    PeopleCreateAPIView,
    PeopleListAPIView,
    test_celery,
    ItemCreate,
    UserRetrieve,
    test_sse,
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import django_eventstream

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("hello/", hello, name="hello"),
    path("form/", form, name="form"),
    path("api/2", people_data, name="api2"),
    path("api/3", people_list, name="api-people"),
    path("api/register", RegisterAPIView.as_view(), name="api-register"),
    path("api/login", LoginAPIView.as_view(), name="api-login"),
    path("api/logout", LogoutAPIView.as_view(), name="api-logout"),
    path("api/data/create", PeopleCreateAPIView.as_view(), name="api-data-create"),
    path("api/data/list", PeopleListAPIView.as_view(), name="api-data-list"),
    path(
        "api/data/update/<int:pk>",
        PeopleUpdateAPIView.as_view(),
        name="api-data-update",
    ),
    path("test/celery", test_celery),
    path("api/item/create", ItemCreate.as_view(), name="api-item-create"),
    # simple jwt
    path(
        "api/token/obtain", TokenObtainPairView.as_view(), name="api-token-obtain-pair"
    ),
    path("api/token/refresh", TokenRefreshView.as_view(), name="api-token-refresh"),
    path("api/user", UserRetrieve.as_view(), name="api-user-retrieve"),
    path("events_trigger/", test_sse, name="sse-test"),
    # path("events/", include(django_eventstream.urls), {"channels": ["test"]}),
]
