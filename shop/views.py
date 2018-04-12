
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import  AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Book, Author, Category
from django.views import generic
from django.views.generic import View
from .forms import UserForm





app_name = 'shop'

# Create your views here.
class ShopBookList(generic.ListView):
    template_name = "index.html"
    model = Book
    paginate_by =9
    def get_context_data(self, **kwargs):
        context = super(ShopBookList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        contacts = Book.objects.filter(year=2018)
        context['name_category'] = 'Новинки'
        paginator = Paginator(contacts, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['contacts'] = file_exams

        return context


class BookList(generic.ListView):
    template_name = "index.html"
    model = Book
    paginate_by = 9
    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        contacts = Book.objects.filter(category__slug=self.kwargs.get('slug'))
        context['name_category'] = Category.objects.get(slug=self.kwargs.get('slug'))
        paginator = Paginator(contacts, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['contacts'] = file_exams
        return context


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'detail_book.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class UserFormView(View):
    form_class = UserForm
    template_name = 'register.html'
    categories = Category.objects.all()

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'categories': self.categories})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('shop:index')

        return render(request,self.template_name,{'form':form})


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/shop"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/shop")



class ProfileSearchView(generic.ListView):
    template_name = 'index.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(ProfileSearchView, self).get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['contacts'] = self.model.objects.filter(title__icontains=query)
        context['query'] = query
        context['name_category'] = "Результаты Вашего поиска:'{}'".format(query)
        context['categories'] = Category.objects.all()
        return context
















