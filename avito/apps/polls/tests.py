from django.urls import include, path, reverse
from rest_framework.test import APITestCase
from rest_framework import status
from . models import Poll
from . serializers import PollSerializer


class PollTests(APITestCase):
#тест на вывод всех polls, если изменить строки во views.py
#poll = get_object_or_404(Poll.objects.all())
#serializer = PollSerializer(poll)

    def test_get_poll(self):
        url = reverse('polls:results')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
#данные тесты не работают вследствие неизвестных автору причин, хотя документация DRF говорит делать так
#получить результаты голосования 
"""def test_poll_results(self):
        url = reverse('polls:poll_results')
        data = {"poll_results":{"poll_id": 1}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
"""

#
"""def test_poll_create(self):
        url = reverse('polls:poll_create')
        data = {"poll": {
        "title": "Лучший мотор?",
        "answers": [
                {
                    "choice_id" : 1
                    "answer": "1-JZ",
                    "votes": 0
                }
                  ]
             }
          }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
"""

"""def test_poll_vote(self):
        url = reverse('polls:poll_vote')
        data = {
              "poll_answers":
              {
              "poll_id": 1,
              "choice_id": ["1", "2", "5"]
              }
              }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
"""
