from django.db import models
from django.urls import reverse

class TennisClub(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    established_date = models.DateField()
    membership_fee = models.IntegerField()

    def __str__(self):
        return self.name

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    join_date = models.DateField()
    tennis_club = models.ForeignKey(TennisClub, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

class Competition(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    tennis_club = models.ForeignKey(TennisClub, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Member)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('comp_detail', args=[str(self.id)])