from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'question',
            'correct_answer',
            'wrong_answer1',
            'wrong_answer2',
            'wrong_answer3',
        )
        model = Question
        