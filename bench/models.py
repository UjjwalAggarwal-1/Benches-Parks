from django.db import models


class Bench1(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Bench2(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Bench1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Bench3(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Bench2, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Park(models.Model):
    bench1 = models.ForeignKey(Bench1, on_delete=models.CASCADE,related_name='park')
    bench2 = models.ForeignKey(Bench2, on_delete=models.CASCADE,related_name='park')
    bench3 = models.ForeignKey(Bench3, on_delete=models.CASCADE,related_name='park')