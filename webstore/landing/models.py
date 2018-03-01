from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)

    def __str__(self):
        try:
            return self.name + ': ' + self.email
        except:
            return 'hernya kakaya-to'