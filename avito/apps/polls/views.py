from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Poll, Answer
from .serializers import PollSerializer, AnswerSerializer
from rest_framework.generics import get_object_or_404


class PollCreate(APIView):
    def post(self, request):
        poll = request.data.get('poll')
        serializer = PollSerializer(data=poll)
        if serializer.is_valid(raise_exception=True):
            poll_saved = serializer.save()
        return Response({"success": "Poll with id={} and title '{}' created successfully".format(poll_saved.id, poll_saved.title)})

class PollVote(APIView):
    def put(self, request):
        data = request.data.get('poll_answers')
        choice_ids = data.get('choice_id')
        poll_id = data.get('poll_id')
        for choice_id in choice_ids:
            saved_poll = get_object_or_404(Answer.objects.all(), poll = poll_id, choice_id = choice_id)
            serializer = AnswerSerializer(instance=saved_poll, data={}, partial=True)
        if serializer.is_valid(raise_exception=True):
            answer_saved = serializer.save()
        return Response({"success": "Voting for answer '{}' with choice_id={} in poll '{}' completed successfully".format(answer_saved.answer, answer_saved.choice_id, answer_saved.poll)})


class PollResults(APIView):
    def post(self, request):
        data = request.data.get('poll_results')
        poll_id= data.get('poll_id')
        poll = get_object_or_404(Poll.objects.all(), id = poll_id)
        serializer = PollSerializer(poll)
        return Response(serializer.data)