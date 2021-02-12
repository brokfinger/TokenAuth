from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .forms import UserRegisterForm
from .models import UserEntranceCount


def home(request):
    return render(request, 'home.html')


def log_in(request, uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode('utf-8')
    username, password = uid.split(',')
    user = User.objects.get(username=username)
    count = UserEntranceCount.objects.get(user_id=user.id)
    count.count += 1
    count.save()

    default_token_generator.check_token(user, token)
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return render(request, 'home.html', {'user': user, 'count': count.count})


def log_out(request):
    logout(request)
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        domain = get_current_site(request)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            count = UserEntranceCount.objects.create(user_id=user.id)
            count.save()

            send_token(form, user, domain)
            return HttpResponse('Проверить почту.')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def send_token(form, user, domain):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    email = form.cleaned_data['email']

    uid = urlsafe_base64_encode(force_bytes(username + ',' + password))
    token = default_token_generator.make_token(user)

    subject = 'Токен для входа.'
    message = render_to_string('email.html', {
        'domain': domain,
        'uid': uid,
        'token': token,
    })
    mail = EmailMessage(subject, message, to=[email])
    mail.send()
