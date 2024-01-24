from django.db import models

# Create your models here.
# to define the structure of database tables
class Record(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.CharField(max_length=70)
  phone = models.CharField(max_length=15)
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  zipcode = models.CharField(max_length=20)

  def __str__(self):
    return(f"{self.first_name} {self.last_name}")


