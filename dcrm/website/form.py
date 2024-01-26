from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record


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
    self.fields['password1'].help_text = '<span class="form-text text-muted"><small><li>Your Password can\'t be too short.</li><li>Your Password can\'t be entirely numeric.</li> <li>Your Password must contain at least 8 characters.</li></small></span>'

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    self.fields['password2'].label = ''
    # if u don't type the right thing for the field a help text pop up 
    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'



# create ADD RECORD form
class AddRecordForm(forms.ModelForm):
  first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
  last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
  email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
  phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number", "class":"form-control"}), label="")
  address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
  city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
  state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
  zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")
  # provide metadata about the form
  class Meta:
    model = Record # specify what model we use: the form is associated with the 'Record' model
    exclude = ("user",) # an easy way to add all the fields >> excluding the "user" field from the form >> won't include an input field for that particular model field