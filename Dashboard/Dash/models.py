from django.db import models

class records(models.Model):
    end_year = models.CharField(max_length=4)
    intensity= models.CharField( max_length=2)
    sector= models.CharField(max_length=12)
    topic= models.CharField(max_length=15)
    insight=models.CharField(max_length=30)
    url= models.CharField(max_length=60)
    region= models.CharField(max_length=30)
    start_year= models.CharField(max_length=4)
    impact= models.CharField(max_length=2)
    added= models.CharField(max_length=30)
    published= models.CharField(max_length=30)
    country= models.CharField(max_length=40)
    relevance= models.CharField(max_length=2)
    pestle= models.CharField(max_length=15)
    source= models.CharField(max_length=25)
    title= models.CharField(max_length=60)
    likelihood= models.CharField(max_length=2)
