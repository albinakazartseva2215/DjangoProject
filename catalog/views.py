from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания продукта"""
    model = Product
    form_class = ProductForm
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        """Метод переопределенный для обработки валидной формы с установкой владельца продукта"""
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для редактирования продукта"""
    model = Product
    form_class = ProductForm
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        """Переопределенный метод для перенаправления после успешного редактирования продукта
        на просмотр этого продукта."""
        return reverse("catalog:product_detail", args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        """Переопределенный метод добавляет пользовательские данные в контекст,
        который передаётся в шаблон при рендеринге"""
        context = super().get_context_data(**kwargs)
        context['title'] = f"Редактирование продукта: {self.object.product_name}"
        return context

    def form_valid(self, form):
        """Обработка валидной формы"""
        # Просто сохраняем форму и перенаправляем на success_url
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        product = self.get_object()
        if user.has_perm("can_unpublish_product"):
            return ProductModeratorForm
        elif product.owner == self.request.user:
            return ProductForm
        else:
            raise PermissionDenied("Вы не являетесь владельцем этого продукта")


class ProductListView(ListView):
    """Класс просмотра списка продуктов"""
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Класс просмотра отдельного продукта"""
    model = Product
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('catalog:products_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Класс удаления отдельного продукта"""
    model = Product
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('catalog:products_list')


class ContactsView(View):
    """Класс представления контактных данных с методом post получения данных пользователя из формы"""

    def get(self, request):
        return render(request, "catalog/contacts.html")

    def post(self, request):
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(name)
        print(message)
        print(phone)

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
