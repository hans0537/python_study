from django.urls import path
from . import views


urlpatterns = [
    path("html/", views.music_html),
    path("json-1/", views.music_json_1),
    path("json-2/", views.music_json_2),
    path("json-3/", views.music_json_3),
    path("<title>/", views.music_title),
]
