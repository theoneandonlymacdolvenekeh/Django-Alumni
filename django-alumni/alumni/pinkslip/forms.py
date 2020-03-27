from django import forms
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    #password feild
    username = forms.CharField()
    #password feild
    password = forms.CharField(widget=forms.PasswordInput)
    # wigdet allows if to viewed as a password

    # clean method makes is that what ever imformation that is being passed in is 
    # the correct information
    def clean(self, *args, **kwargs):
        # this gets the username 
        username = self.cleaned_data.get('username')
        # this gets the password
        password = self.cleaned_data.get('password')

        # this is were it does the checks
        # if there is a username and password then authenticated it 
        # check that the username and password exist it the database
        if username and password:
            # authenicate method takes in two variables, username and password
            # and then chaecks it
            # returns a boolean, ture or false
            user = authenticate(username=username, password=password)
            # if user information is false
            # then there would be a validaiton error
            if not user:
                raise forms.ValidationError('this user does not exist')
            # if the password is a wrong
            # then there would be a validaiton error
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            # if the user is not active
            # then there would be a validaiton error
            if not user.is_active:
                raise forms.ValidationError('this is not active')
            #
        return super(UserLoginForm, self).clean(*args, **kwargs)    


class DataInput(forms.DateInput):
    input_type= 'date'

from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import profile
from django.forms.widgets import DateInput


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
class StudentProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout (
            Row(
                
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('date_of_birth', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            
            Submit('submit', 'confirm')
        )


    class Meta:
        model = profile
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
        }
        exclude = (
            'user',
        )
        



# class User form
# Class profile form
# In templates {% user_form %}
# If not is_staff: {% studentForm %}
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'email'
        )        