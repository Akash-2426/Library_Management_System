from django.db import models


# Create your models here.
class Add_a_book(models.Model):
    bname = models.CharField(max_length=50, name=False)
    bcode = models.IntegerField(default=0)
    add_date = models.DateField()

class Update_an_entry_of_a_book(models.Model):
    bname = models.CharField(max_length=50, name=False)
    bcode = models.IntegerField(default=0)
    issuedate = models.DateField()

class Delete_a_book(models.Model):
    bname = models.CharField(max_length=50, name=False)
    bcode = models.IntegerField(default=0)

class Get_all_book(models.Model):
    bname = models.CharField(max_length=50, name=False)
    bcode = models.IntegerField(default=0)


