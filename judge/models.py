from django.db import models

# Create your models here.
class Problems(models.Model):
    name = models.CharField(max_length=200)
    statement = models.CharField(max_length= 300)
    difficulty = models.CharField(max_length=200)
    code = models.CharField(max_length= 255)
    def __str__(self):
        return  self.name

class Solutions(models.Model):
    verdict = models.CharField(max_length = 200)
    submitted_at = models.DateTimeField(max_length=200)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)

    def __str__(self):
        return self.verdict

class TestCases(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    input = models.CharField(max_length=255)
    output = models.CharField(max_length=255)

    def __str__(self):
        return self.input
