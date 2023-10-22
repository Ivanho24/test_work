from django.contrib import admin
from django.urls import path
from app.views import upload_json,show_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_json, name='upload_json'),
    path('data/',show_data, name='show_data'),    
]
