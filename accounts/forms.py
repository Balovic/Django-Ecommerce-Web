from django import forms
from .models import Account
import re
from django.utils.translation import ugettext as _

# class MySetPasswordForm(SetPasswordForm):
    
#     def __init__(self, *args, **kwargs):
#         super(MySetPasswordForm, self).__init__(*args, **kwargs)
#         self.fields['new_password1'].validators.append(NumberValidator)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter your phone number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if not re.findall('\d', password):
            raise forms.ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )
                
        if not re.findall('[A-Z]', password):
            raise forms.ValidationError(
                _("The password must contain at least 1 uppercase letter, from A-Z."),
                code='password_no_upper',
            )    
            
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise forms.ValidationError(
                _("The password must contain at least 1 special character: " + 
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )
        
        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
        return self.cleaned_data
        
    
        
        