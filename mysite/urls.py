from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include("polls.urls")), # 8000/polls url에서 동작
    path('admin/', admin.site.urls),
]
