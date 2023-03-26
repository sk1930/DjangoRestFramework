from django import forms 
from .models import Review
from django.forms import ModelForm

'''
class ReviewForm(forms.Form):
    # we put the fields to be displayed on the form here
    first_name =forms.CharField(label="First_Name",max_length=100)
    last_name =forms.CharField(label="Last_Name",max_length=100)
    email =forms.EmailField(label="Email")
    # if u try to fill a email of wrong format the EmailField takes care of validation
    # and doesnt allow to submit
    review =forms.CharField(label="Please write your review here",
                                widget=forms.Textarea(attrs={'class':'myform','rows':'6','cols':'8'}))
                                #attrs is a dictionary myform style  will be applied run time from custom.css
                                # we can add more attributes like rows and cols
                                # like below
                                #<textarea id="w3review" name="w3review" rows="4" cols="50">
                                # u can goto w3schools or any and look for the tag and add them to the dictionary
                                #https://www.w3schools.com/tags/tag_textarea.asp
'''
# below code automatically c
# creates form fields form the model just like above where we created manually
#https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        #fields = ['first_name','last_name','stars']
        # form shows on the fields in the fields list above
        # instead of passing as above u can say __all__
        fields = "__all__"

        # u can also give custom names for the form labels like below
        # modelfieldname :  customname
        labels = {'first_name':"Enter First Name here",
        'stars':'Rating'}
        # as i not entered last name here  , last_name will be same from the model
        # ie form shows the name  last_name as Last name -- like caps first and _ replaced with space
        
        # lets add validators  to models.py 


        # lets add custom error messages 
        error_messages = {
            'stars':{
             'min_value': 'min value should be 1',
             'max_value':'max value should be 5'

            }
        }




                    