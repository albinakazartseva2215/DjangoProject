from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import ArticleForm
from blog.models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        """Возвращает только опубликованные статьи"""
        return super().get_queryset().filter(
            is_published=True
        ).order_by('-created_at')  # Сортировка по дате создания


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(self.queryset)
        self.object.views_count += 1
        self.object.save(update_fields=['views_count'])
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("blog:blog_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Редактирование продукта: {self.object.title}"
        return context

    def form_valid(self, form):
        """Обработка валидной формы"""
        # Просто сохраняем форму и перенаправляем на success_url
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:blog_list")


class ContactsView(View):

    def get(self, request):
        return render(request, "blog/contacts.html")

    def post(self, request):
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(name)
        print(message)
        print(phone)

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
