from django.db import models

# Create your models here.
class Physician(models.Model):
    npi = models.PositiveIntegerField(help_text="A number between 1000000000 and 19999999999",
                             primary_key=True)
    board_cert = models.BooleanField(help_text="Whether or not the doctor is board certified",
                                     default=False)
    age = models.PositiveSmallIntegerField(help_text="The doctors age")
    rating = models.PositiveSmallIntegerField(help_text="A rating from 1 to 5",
                                              default=4)
    language = models.CharField(help_text="The doctors most proficient language",
                                default="English",
                                max_length=256)
    location = models.CharField(help_text="The primary office location of this doctor",
                                max_length=256)
