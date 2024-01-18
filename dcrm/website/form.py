from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# the class SignUpForm inherite UserCreationForm
class SignUpForm(UserCreationForm): 
  first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),max_length=30, required=False)

  last_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),max_length=30)

  email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}),required=True)

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# we do the same things we did above for fist name, last name, and email. but here for username, password1, and password2
  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs) # Call the parent's constructor

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
    self.fields['username'].label = ''
    # if u don't type the right thing for the field a help text pop up 
    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password1'].label = ''
    # if u don't type the right thing for the field a help text pop up 
    self.fields['password1'].help_text = '<span class="form-text text-muted small"><li>Your Password can\'t be too short.</li></span>'

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    self.fields['password2'].label = ''
    # if u don't type the right thing for the field a help text pop up 
    self.fields['password2'].help_text = '<span class="form-text text-muted><small>Enter the same password as before, for verification.</small></span>'
  