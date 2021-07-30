from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from . import forms
from .models import Refill, Tag
from .models import Tap

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
                user = User.objects.create_user(form.cleaned_data["username"], '', form.cleaned_data["username"])
                if form.cleaned_data["name"] != "":
                    user.first_name = form.cleaned_data["name"]
                user.save()
                players = Group.objects.get(name='players') 
                players.user_set.add(user)
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


def dashboard(request):
    taps = Tap.objects.all()
    taps_d = []
    for tap in taps:
        if tap.onTap is not None:
            taps_d.append({'tap': tap, 'remaining': tap.onTap.remaining()})

    players = User.objects.filter(groups__name='players', is_active=True)

    players_d = []

    for player in players:
        refills = Refill.objects.filter(user=player)
        volume = 0
        drinks = 0
        for refill in refills:
            drinks += 1
            volume += refill.container.capacity

        if player.first_name == "":
            name = player.username
        else:
            name = player.first_name

        volume_m = None
        if volume < 1:
            volume_m = volume*1000


        players_d.append({'name': name, 'username': player.username, 'reffils': drinks, 'volume': volume, 'volume_m': volume_m})

    players_d.sort(key=lambda x: x.get('volume'), reverse=True)

    return render(request, 'dashboard.html', {'taps': taps_d, 'players': players_d})
