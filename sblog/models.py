from django.db import models
class sb(models.Model):
    title=models.CharField(max_length=200)
    p_date=models.DateTimeField()
    text=models.TextField()
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100]
    def pub_date_pretty(self):
        return self.p_date.strftime('%b %e %Y')
