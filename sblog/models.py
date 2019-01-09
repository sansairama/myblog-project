from django.db import models
class sb(models.Model):
    title=models.CharField(max_length=200)
    p_date=models.DateTimeField()
    text=models.TextField()
    image=models.ImageField(upload_to='images/')
