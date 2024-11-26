from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from core.models import Profile

from .models import Order
from .models import Profile

class OrderForm(ModelForm):
  class Meta:
    model = Order
    fields = '__all__'
    
class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    
class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # Menambahkan email field di form

    class Meta:
        model = Profile
        fields = ['profile_picture', 'organization_name', 'address', 'phone_number', 'birthday', 'email']  # Menambahkan email ke fields

    def save(self, commit=True):
        # Mengupdate email pada user yang terkait
        instance = super().save(commit=False)
        instance.user.email = self.cleaned_data['email']
        if commit:
            instance.user.save()
            instance.save()
        return instance