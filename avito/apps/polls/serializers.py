from rest_framework import serializers
from . models import Poll, Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('choice_id', 'answer', 'votes')

    def update(self, instance, validated_data):
        instance.votes+=1
        instance.save()
        return instance


class PollSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('title', 'answers')

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        poll = Poll.objects.create(**validated_data)
        for answer_data in answers_data:
            Answer.objects.create(poll=poll, **answer_data)
        return poll