from django.db import models

class Selection(models.Model):
    selection_text = models.CharField(max_length = 200)

    def __str__(self):
        return self.selection_text

class Inputdata(models.Model):
    selection = models.ForeignKey(Selection)
    fingerprint = models.ImageField(height_field=None,width_field=None,max_length=100)
    input_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.input_name

class Iddata(models.Model):
    inputdata = models.ForeignKey(Inputdata)
    name = models.CharField(max_length=50)
    idnumber = models.IntegerField()
    sex = models.IntegerField()
    address = models.CharField(max_length=200)
    finger = models.ImageField()
