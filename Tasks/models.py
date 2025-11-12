from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField()
    tags = models.ManyToManyField('Tag', related_name='tasks', blank=True)



    def __str__(self):
        return self.title

   

class Tag(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name