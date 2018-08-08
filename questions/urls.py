from django.urls import path
from .views import *

urlpatterns = [
    path('', ListQuestions.as_view()),
    path('<int:pk>/', DetailQuestion.as_view()),
]