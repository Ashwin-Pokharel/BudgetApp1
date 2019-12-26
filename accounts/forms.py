from .models import Expense,Incomes
from django.contrib.auth.models import User
from .models import Category as CategoryModel
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignInForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=False)
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2',)

class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())


class Expense_form(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ('user',)
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, user, *args, **kwargs):
        super(Expense_form, self).__init__(*args, **kwargs)
        systemUser = User.objects.get(username = 'system')
        try:
            systemCategories = CategoryModel.object.filter(user = systemUser , type = 'E')
            self.fields['category'].queryset = (CategoryModel.object.filter(user=user , type = 'E') | systemCategories)
        except:
            systemCategories = CategoryModel.object.filter(user=systemUser, type='E')
            self.fields['category'].queryset = systemCategories




class Income_form(forms.ModelForm):
    class Meta:
        model = Incomes
        exclude = ('user',)
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


    def __init__(self, user, *args, **kwargs):
        super(Income_form, self).__init__(*args, **kwargs)
        systemUser = User.objects.get(username='system')
        systemCategories = CategoryModel.object.filter(user=systemUser , type = 'I')
        self.fields['category'].queryset = CategoryModel.object.filter(user=user , type = 'I') | systemCategories


class Category_form(ModelForm):
    class Meta:
        model = CategoryModel
        exclude = ('user',)
