from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Physician(models.Model):
    npi = models.PositiveIntegerField(help_text="A number between 1000000000 and 1999999999",
                                      primary_key=True,
                                      validators=[MaxValueValidator(1999999999), MinValueValidator(1000000000)])

    board_cert = models.BooleanField(help_text="Whether or not the doctor is board certified",
                                     default=False)

    age = models.PositiveSmallIntegerField(help_text="The doctors age")

    rating = models.PositiveSmallIntegerField(help_text="A rating from 1 to 5",
                                              default=4,
                                              validators=[MaxValueValidator(5), MinValueValidator(1)])

    language = models.CharField(help_text="The doctors most proficient language",
                                default="English",
                                max_length=256)

    location = models.CharField(help_text="The primary office location of this doctor",
                                max_length=256)

    # the model to hold the results of the rules engine
    rule_results = models.CharField(blank=True,
                                    editable=False,
                                    max_length=256)

    def __str__(self):
        return("""NPI: %s\n
                  Board Cert: %s\n
                  Age: %d\n
                  Language: %s\n
                  Location: %s\n
                  Rating: %d\n""" % (self.npi, self.board_cert, self.age, self.language, self.location, self.rating))
