from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from .models import *


# Create your views here.
def kayitol(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            kullaniciadi = form.cleaned_data.get('username')
            messages.success(request, f'Hesabınız başarıyla oluşturuldu: {kullaniciadi} , tekrar giriş yapınız.')
            return redirect('forumapp:anasayfa')
    else:
        form = UserRegisterForm()

    return render(request, 'kullanicilar/kayitol.html', {'form': form})

pass

def girisyap(request):

    if request.user.is_authenticated:
        return redirect('forumapp:anasayfa') 

    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            username = User.objects.get(email = email).username

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('forumapp:anasayfa')

            else:
                return render(request, 'kullanicilar/girisyap.html', {
                    'form': form
                })
        else:
            return render(request, 'kullanicilar/girisyap.html', {
                    'form': form
                })
    else:
        form = UserLoginForm()
        return render(request, 'kullanicilar/girisyap.html', {
            'form': form
        })

@login_required
def cikisyap(request):
    logout(request)
    return redirect('forumapp:anasayfa')

@login_required
def profiles_view(request):
    profile = Profil.objects.filter(kullanici = request.user)
    return render(request, 'kullanicilar/profiles.html',{
        'profile':profile
    })

@login_required
def profile_add_view(request):

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.kullanici = request.user
            profile.save()
            return redirect('profiles_page')
        else:
            return render(request, 'kullanicilar/profiles.html', {
                'form': form
            })

    form = UserProfileForm()
    return render(request, 'kullanicilar/profile_add.html', {
        'form': form
    })


@login_required
def profile_edit(request, profil_slug):
    profile = Profil.objects.get(slug=profil_slug)
    formu = UserEditForm(instance=request.user)
    formp = ProfilEditForm(instance=profile)
    if request.method == 'POST':
        formu = UserEditForm(request.POST, instance=request.user)
        formp = ProfilEditForm(request.POST, request.FILES, instance=request.user.profil)

        if formu.is_valid() and formp.is_valid():
            formu.save()
            profile = formp.save(commit=False)
            profile.kullanici = request.user
            profile.save()
            messages.success(request, f'Hesabınız Güncellenmiştir.')
            return redirect('profiles_page')
        else:
            return render(request, 'kullanicilar/profile_edit.html', {
                'formu': formu,
                'formp': formp,
                'profile': profile
            })

    return render(request, 'kullanicilar/profile_edit.html', {
        'formu': formu,
        'formp': formp,
        'profile': profile
    })


@login_required
def change_password_view(request):

    if request.method == 'POST':
        form = ChangeUserPassword(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('kullanicilar/profiles.html')
        else:
            return render(request, 'kullanicilar/change_password.html', {
                'form': form
            })
    
    form = ChangeUserPassword(request.user)
    return render(request, 'kullanicilar/change_password.html', {
        'form': form
    })