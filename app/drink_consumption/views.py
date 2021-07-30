from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

from django.db import IntegrityError

from . import forms
from .models import Tag

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.RegisterForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)

            user_free = False
            tag_free = False

            try:
                User.objects.get(username=form.cleaned_data["username"])
            except User.DoesNotExist:
                user_free = True

            try:
                Tag.objects.get(uid=form.cleaned_data['tag_id'])
            except Tag.DoesNotExist:
                tag_free = True

            if user_free and tag_free:
                user = User.objects.create_user(form.cleaned_data["username"], '', '')
                if form.cleaned_data["name"] != "":
                    user.first_name = form.cleaned_data["name"]
                user.save()
                Tag.objects.create(uid=form.cleaned_data['tag_id'], owner=user, description="").save()
                return render(request, 'super-nickel.html')
            
            if not user_free:
                form.add_error("username", "user already exist")

            if not tag_free:
                form.add_error("tag_id", "tag exist")

            return render(request, 'register.html', {'form': form})

    else:
        form = forms.RegisterForm()

    return render(request, 'register.html', {'form': form})
