from django.urls import path
from .views import Main
from django.contrib import admin
urlpatterns = [
    path('', Main.as_view()),
    path('admin/', admin.site.urls),
]