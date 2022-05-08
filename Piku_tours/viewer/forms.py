from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Rate


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    birth_day = forms.DateField(widget=forms.SelectDateWidget(years=list(range(1900,2022))), required=False, label='Date of Birth')
    message = forms.CharField(max_length=500, widget=forms.Textarea)

class RegisterUserForm(UserCreationForm):

    def save(self):
        new_user = super().save()
        new_profile = Profile.objects.create(user=new_user)
        return new_user

class RateTravelForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields = '__all__'
        widgets = {
            'profile': forms.HiddenInput(),
            'travel': forms.HiddenInput()
        }