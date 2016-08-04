# -*- coding: utf-8 -*-
from .forms import UserLoginForm,SignUpForm,UserRegisterForm,File_form, UploadFileForm, ContactForm
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView, ListView
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib import messages




def home(request):
    title="my title"
    form = SignUpForm(request.POST )
    context = {
        "title":title,
        "form":form
    }

    if form.is_valid():

        form.save()
    return render(request, "home.html", context)

def upload_file(request):
    user= request.user
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        doc = form.save(commit=False)
        doc.user = request.user
        doc.save()
        messages.success(request, 'Dosya Yuklendi')

        return HttpResponseRedirect('/uploadnew/')
    
    return render(request, 'upload.html', {'form': form})



def contact(request):
    user= request.user
    next = request.GET.get('next')
    title = "Kişisel Bilgiler"
    form = ContactForm(request.POST or None)

    context = {
        "title":title,
        "form":form
    }

    if form.is_valid():
        Contact = form.save(commit=True)
        Contact.user = request.user

        Contact.save()
        return redirect("/uploadnew")
    return render(request, "form.html", context)


def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Giriş Ekranı"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        messages.success(request, 'Giris Onaylandi')

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/uploadnew")
    return render(request, "login_page.html", {"form":form, "title": title})

def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Kayıt Ekranı"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        form.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/kaydol")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "form.html", context)

def file_view(request):
    form = File_form(request.POST or None, request.FILES or None )
    if form.is_valid(): 
        form.save()
        instance = form.save(commit= False)
        instance.save()
        return redirect("/")
    context = {"form":form,
    }
    return render(request, "form.html", context)



def logout_view(request):
    logout(request)
    messages.success(request, 'Cikis Basarili')

    return redirect("/login")







from .models import Contact, MyUser

from .forms import ContactForm, UserRegisterForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import CreateView

"""class TotalRegister(CreateView):
    template_name = 'total_register.html'
    form_class = UserRegisterForm

    def form_valid(self, form, ContactForm):
        context = self.get_context_data()
        sponsorships = context['sponsorships']
        with transaction.commit_on_success():
            form.instance.created_by = self.request.user
            form.instance.updated_by = self.request.user
            self.object = form.save()
        if sponsorships.is_valid():
            sponsorships.instance = self.object
            sponsorships.save()



"""


"""
def total_register(request):
    uform = UserRegisterForm()
    cform = ContactForm()
    if request.method == "POST":
        uform = UserRegisterForm(request.POST , instance=User())
        cform = [ContactForm(request.POST , prefix=str(x), instance=Contact()) for x in range(0,1)]
        if uform.is_valid() and all([cf.is_valid() for cf in cform]):

            new_MyUser = uform.save()
            new_MyUser = authenticate(username=User.username, password=password, lastname = lastname)
            for cf in cform:
                new_contact = cf.save(commit=False)
                new_contact.MyUser = new_MyUser
                new_contact.save()
            return HttpResponseRedirect('/')
    else:
                                pform = UserRegisterForm(instance=User())
                                cform = [ContactForm(prefix=str(x), instance=Contact()) for x in range(0,1)]
    return render_to_response('total_register.html', {'UserRegisterForm': uform, 'ContactForm': cform},context_instance=RequestContext(request))"""


