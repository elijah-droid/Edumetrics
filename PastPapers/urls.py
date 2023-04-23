from django.urls import path
from .views import parent_view_pastpapers, teachers_pastpapers, upload_pastpaper, download_pastpaper


urlpatterns = [
    path('parents-view/', parent_view_pastpapers, name="parent-pastpapers"),
    path('teachers-pastpapers/', teachers_pastpapers, name="pastpapers"),
    path('upload/', upload_pastpaper, name="upload-pastpaper"),
    path('download/<int:paper>/', download_pastpaper, name='download-paper')
]