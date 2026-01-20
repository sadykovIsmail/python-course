# polls/polls/urls.py (project-level)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # include your app's urls
]
