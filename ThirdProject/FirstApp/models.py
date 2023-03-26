from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
# the classes here represent the tables and the fields represent the columns
# https://docs.djangoproject.com/en/4.1/ref/models/fields/
# IN ABOVE URL we ahave all field details
# 
#we have fields like autoNow --- to automatically fill current time absed on button click
#charfield, integerfield
#there are some validations also like MinValueValidator, maxValueValidator in the same page


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # MinValueValidator == limit_value: Any, message: _ErrorMessage | None = ...) -> None
    age  = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120,"age cannot be more than 120")])
    heartrate = models.IntegerField(default=60,validators=[MinValueValidator(1),MaxValueValidator(300,"heartrate cannot be more than 300")])
    def __str__(self):
        return f"{self.first_name} and {self.last_name} his age = {self.age}"

