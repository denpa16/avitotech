from django.urls import path
from .views import PollVote, PollCreate, PollResults

app_name = "polls"

urlpatterns = [
    path('createPoll/', PollCreate.as_view(), name='poll_create'),
    path('poll/', PollVote.as_view(), name='poll_vote'),
    path('getResult/', PollResults.as_view(), name="poll_results"),
]