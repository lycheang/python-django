from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
class Choice(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text
class Vote(models.Model):

    choice = models.ForeignKey(Choice,related_name='votes', on_delete=models.CASCADE)
    account = models.ForeignKey(Account,related_name='votes', on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('account', 'vote_by')

        