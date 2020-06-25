"""asker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'polls', views.PollsView, basename='poll')
router.register(r'questions', views.QuestionsView, basename='question')
urlpatterns = router.urls

urlpatterns += [
    re_path('admin/', admin.site.urls),
    re_path(r'^start_polls/$', views.PollsAnswer.as_view(), name='start'),
    re_path(r'^result_polls/$', views.PollsResult.as_view(), name='result'),
    re_path(r'^$', views.Input.as_view()),
]
