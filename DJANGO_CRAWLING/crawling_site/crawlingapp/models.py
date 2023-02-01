from django.db import models

# Create your models here.
class NewsTitle(models.Model):
    site_name = models.CharField(max_length=30)
    news_title = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.site_name}의 뉴스 제목 {self.news_title}'


# Create your models here.
# class Passenger(models.Model):
#     name = models.CharField()
#     sex = models.CharField()
#     survived = models.BooleanField()
#     age = models.FloatField()
#     ticket_class = models.PositiveSmallIntegerField()
#     embarked = models.CharField()