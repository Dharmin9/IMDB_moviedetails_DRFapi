from django.contrib import admin
from django.urls import path
from mdetail import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.movie_detail.as_view(), name="api page"),
]

# api URL = " http://127.0.0.1:8000/movieapi/"