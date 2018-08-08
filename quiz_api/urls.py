from django.contrib import admin
from django.urls import path, include
from questions import urls as question_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/', include(question_urls)),
]







