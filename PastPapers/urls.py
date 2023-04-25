from django.urls import path
from .views import browse_pastpapers, teachers_pastpapers, upload_pastpaper, download_pastpaper


urlpatterns = [
    path('browse/', browse_pastpapers, name="browse-pastpapers"),
    path('teachers-pastpapers/', teachers_pastpapers, name="pastpapers"),
    path('upload/', upload_pastpaper, name="upload-pastpaper"),
    path('download/<int:paper>/', download_pastpaper, name='download-paper')
]