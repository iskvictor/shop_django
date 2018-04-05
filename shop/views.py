from django.shortcuts import render,render_to_response,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book, Author, Category
from django.views import generic


app_name = 'shop'

# Create your views here.
#def index(request):
   # categories = Category.objects.all()
   # contact_list = Book.objects.all()
    #paginator = Paginator(contact_list, 20)
    #page = request.GET.get('page')
    #try:
        #contacts = paginator.page(page)
    #except PageNotAnInteger:
       # contacts = paginator.page(1)
    #except EmptyPage:
       # contacts = paginator.page(paginator.num_pages)
    #return render_to_response('index.html', {"contacts": contacts, 'categories': categories})


#class ddBookList(generic.ListView):
   # template_name = "index.html"
   # context_object_name = 'contacts'
    #def get_queryset(self):
        #return Book.objects.filter(category__slug=self.kwargs.get('slug'))

class ShopBookList(generic.ListView):
    template_name = "index.html"
    model = Book
    paginate_by = 1
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
    model = Category
    paginate_by = 2
    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        contacts = Book.objects.filter(category__slug=self.kwargs.get('slug'))
        context['name_category']=Category.objects.get(slug=self.kwargs.get('slug'))
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

#def detail(request, slug):
    #print('print',slug)
    #details = "test.html"
    #context = {
       # "contacts": Book.objects.filter(category__slug=slug)
    #}
    #return render(request, details, context)




