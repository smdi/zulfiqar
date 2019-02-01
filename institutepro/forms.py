from django import forms
from multiselectfield import MultiSelectFormField
from .porter import  *
from .models import RegistrationData
from django.forms.widgets import SelectDateWidget
from django.core import validators

class RegistrationForm(forms.Form):

    username = forms.CharField(
        # label='username',
        widget=forms.TextInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'enter a user name'

            }

        )

    )
    email = forms.EmailField(

        # label='email',
        widget=forms.EmailInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'email your email'

            }

        )
    )
    password1 = forms.CharField(

        label='Password',
        widget=forms.PasswordInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'enter password'

            }
        )
    )
    password2 = forms.CharField(

        label='Re-enter password',
        widget=forms.PasswordInput(

            attrs={
                'class': 'form-control',
                'placeholder': 're enter password'

            }
        )
    )
    # dob = forms.DateField(
    #
    #     label='dob',
    #     widget=forms.DateInput(
    #
    #         attrs={
    #             'class': 'form-control',
    #             'place-holder': 'password'
    #
    #         }
    #     )
    # )
    mobile = forms.IntegerField(

        # label='mobile',
        widget=forms.NumberInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'enter mobile number'

            }
        )
    )

def check_users(value):
    if value[0].lower() != 'd':
        print('must start with d')
        raise forms.ValidationError('must start with d')


class LoginForm(forms.Form):

    username = forms.CharField( validators = [check_users] ,
        # label='username',
        widget=forms.TextInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'enter username'

            }

        )



    )
    password = forms.CharField(

        # label='password',
        widget=forms.PasswordInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'enter password'

            }
        ),

    )
    def clean_username(self):
        username = self.cleaned_data['username']
        print('in clean username '+username)
        if len(username) <=0 :
             print('username error')
             raise forms.ValidationError('check ur username')
        return username




class ForgotPasswordForm(forms.Form):

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'enter your username'

            }

        )

    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(

            attrs={
                'class': 'form-control',
                'placeholder': 'enter new password'

            }

        )

    )
    password2 = forms.CharField(

        label='Re enter password',
        widget=forms.PasswordInput(

            attrs={
                'class': 'form-control',
                'placeholder': 're enter password'

            }
        )
    )



class ApplicantForm(forms.Form):
    name  = forms.CharField(
        # label= 'name' ,
        widget=forms.TextInput (
            attrs={

                'placeholder': 'enter your name',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(

        # label='email',
        widget=forms.EmailInput(

            attrs={
                'placeholder': 'enter your email id',
                'class': 'form-control'


            }

        )
    )
    mobile = forms.IntegerField(

        # label= 'mobile' ,

        widget= forms.NumberInput(

            attrs= {
                'placeholder': 'enter your mobile number',
                'class' : 'form-control'

            }


        )
    )

    courses = MultiSelectFormField(max_length= 100 , choices= COURSE__CHOICES)
    timings = MultiSelectFormField(max_length=100, choices=TIMING__CHOICES)
    years = range(2018,1970 , -1)
    startdate = forms.DateField(

       widget=forms.widgets.SelectDateWidget(years=years)
    )


class FeedbackForm(forms.Form):

    name = forms.CharField(

        label= 'Name' ,
        widget= forms.TextInput(

            attrs= {

                'class' :'form-control' ,
                'placeholder' :'enter your name'
            }
        )
    )


    ratings = forms.IntegerField(

    label='Ratings',
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'give ratings from 1 - 5'
            }
        )
    )


    feedback = forms.CharField(

    label='Feedback',
    widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'give your feedback short and descriptive'
            }
        )
    )
