"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from solution.views import chatgpt_api

from rest_framework import routers
from instagrams.views import getcrawling, PostListView

# router = routers.DefaultRouter()
# router.register('posts', PostView)

urlpatterns = [
    # path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('chatgpt-api/', chatgpt_api, name='chatgpt_api'),
    path('getcrawling/', getcrawling, name='getcrawling'),
    path('event/', PostListView.as_view(),),
]
