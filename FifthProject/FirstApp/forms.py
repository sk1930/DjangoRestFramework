from django import forms 

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