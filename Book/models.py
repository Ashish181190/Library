from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    is_deleted = models.CharField(max_length= 1, default= 1)

    def __str__(self):    
        return f"{self.__dict__}"
        
    class Meta:
        db_table = "book"
        