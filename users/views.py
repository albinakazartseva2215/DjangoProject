import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    """Класс создания пользователя"""
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Метод переопределенный для регистрации пользователя с отправкой на почту ссылки для подтверждения"""
        user = form.save()
        user.is_active = False  # пользователь не сможет войти, пока не активирует аккаунт
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    """метод, который обрабатывает подтверждение email по токену"""
    user = get_object_or_404(User, token=token)
    user.is_active = True  # активирует учётную запись пользователя
    user.save()
    return redirect(reverse("users:login"))
