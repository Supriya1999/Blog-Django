from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Blog,Category
from django.views.generic import ListView, DetailView, UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
# def home(request):
#     return render(request,'blog_app/home.html')

# def about(request):
#     return render(request,'blog_app/about.html')

# def contact(request):
#     return render(request,'blog_app/contact.html')

# def dashboard(request):
#     return render(request,'blog_app/dashboard.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/home')
        else:
            form = LoginForm()
        return render(request,'blog_app/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/home')
    

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        f = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'blog_app/login.html',{'f':f})
    else:
        form = SignUpForm()
    return render(request,'blog_app/signup.html', {'form':form})

def user_logout(request):
    logout(request)
    return render(request,'blog_app/home.html')

def CategoryView(request,cats):
    category_posts=Blog.objects.filter(category=cats.replace('-',' '))
    return render(request,'blog_app/categories.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})


class IndexView(ListView):
    model = Blog
    template_name = 'blog_app/home.html'
    cats = Category.objects.all()

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(IndexView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
    

class SingleView(DetailView):
    model = Blog
    template_name = 'blog_app/single.html'
    context_object_name = 'post'

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(SingleView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostsView(ListView):
    model : Blog
    template_name = 'blog_app/dashboard.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Blog.objects.all()


class AddView(CreateView):
    model = Blog
    template_name = 'blog_app/add.html'
    fields = '__all__'
    success_url = reverse_lazy('blog_app:posts')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog_app/addcategory.html'
    fields = '__all__'
    success_url = reverse_lazy('blog_app:posts')


class EditView(UpdateView):
    model = Blog
    template_name = 'blog_app/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'
    success_url = reverse_lazy('blog_app:posts')


class Delete(DeleteView):
    model = Blog
    template_name = 'blog_app/confirm_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog_app:posts')


