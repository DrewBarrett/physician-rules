from django.db import models

# Create your models here.
class Physician(models.Model):
    npi = models.PositiveInt(help_text="A number between 1000000000 and 19999999999",
                             primary_key=True)
    board_cert = models.