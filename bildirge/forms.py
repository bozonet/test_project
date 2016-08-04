# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

from .models import  SignUp, MyUser, MyUserManager, Doc ,Contact
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
User = get_user_model()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email','full_name']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['unvan','isim','soyad','kurum',"bolum","gorev", "uzmanlik","adres","posta_kodu","sehir","ulke","is_tel","ev_tel","fax_no","cep_tel"]


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['unvan'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['isim'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['soyad'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['kurum'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['gorev'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['uzmanlik'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['adres'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['posta_kodu'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['sehir'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['ulke'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['is_tel'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['ev_tel'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['fax_no'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['cep_tel'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}


        """def clean(self):
                                    form_data = self.cleaned_data
                                    if form_data['sifre'] != form_data['sifre_onay']:
                                        self._errors["sifre"] = ["Password do not match"] # Will raise a error message
                                        del form_data['sifre']"""
    #return form_data




class UserRegisterForm(forms.ModelForm):
    username = forms.EmailField(label = 'Mail',error_messages={'required': 'Bu alan doldurulmalıdır'})

    password = forms.CharField(widget=forms.PasswordInput, label = 'Şifre',error_messages={'required': 'Bu alan doldurulmalıdır'})

    password2 = forms.CharField(widget=forms.PasswordInput, label = 'Şifrenizi Onaylayın',error_messages={'required': 'Bu alan doldurulmalıdır'})



    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2'
          
            ]
    #RegisterFormset = inlineformset_factory(User, Contact)
    """def signup(self, request, user):
                    user.username = self.cleaned_data['username']
                    user.lastname = self.cleaned_data['lastname']
            
            
                    user.save()
            """
    
    def clean_password2(self):
                    password = self.cleaned_data.get('password')
                    password2 = self.cleaned_data.get('password2')
                    if password != password2:
                        raise forms.ValidationError("passwords must match")
        
class File_form(forms.ModelForm):
    document = forms.FileField(label='Dosya yukleyiniz')
    class Meta:
        model = User
        fields = ['document',]


class UserLoginForm(forms.Form):
    username = forms.EmailField(label = "Mail")
    password = forms.CharField(widget=forms.PasswordInput, label = 'Şifre')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
       
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Böyle bir kullanıcı yok")
            if not user.check_password(password):
                raise forms.ValidationError("Yanlış Şifre")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)





class UploadFileForm(ModelForm):
    class Meta:
        model = Doc
        fields = ('Dosya','Etkinlik',)
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['Dosya'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}
        self.fields['Etkinlik'].error_messages = {'required': 'Bu alan doldurulmalıdır!'}

