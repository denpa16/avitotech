from django.db import models


class Poll(models.Model):
    """Голосование"""
    title = models.CharField(max_length=200,verbose_name = "Голосование")

    def __str__(self):
        return self.title
 
    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'
  
 
class Answer(models.Model):
    """Вариант ответа на голосование"""
    poll = models.ForeignKey(Poll, related_name = 'answers', on_delete = models.CASCADE)
    choice_id = models.IntegerField(verbose_name = "Порядковый номер в голосовании")
    answer = models.CharField(max_length=200, verbose_name = "Ответ")
    votes = models.IntegerField(verbose_name = "Голосов", default = 0)
 
    def __str__(self):
        return self.answer
 
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'