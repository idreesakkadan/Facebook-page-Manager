from django.db import models
# from djangoratings.fields import RatingField


# Create your models here.
class Pages(models.Model):
    source = models.CharField(max_length=100)
    page_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
    # rating = modes.RatingField(range=5) # 5 possible rating values, 1-5
    listed = models.BooleanField()
