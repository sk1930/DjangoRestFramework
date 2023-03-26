from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    stars =models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])
    # these validators are automatically  checked in views.py in if form.is_valid
    # as all these validators are added make migration and run migrations
    # now if u click submit by filling rating as 9
    # it doesnt do anything becoz the data is not valid but it is not reporting any error
    # to report the error usse {{field.errors}} in the rental_review.html
    # now if u fill  7 it automaticalkly shows the error message as Ensure this value is less than or equal to 5.
    # if u fill 0 it shows  Ensure this value is greater than or equal to 1.

    # 