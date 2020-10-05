from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Tag
from .forms import PostForm, TagForm, AuthUserForm


class UserLoginView(LoginView):
    template_name = 'blog/login_form.html'
    success_url = reverse_lazy('posts_list_url')
    form_class = AuthUserForm

    def get_success_url(self):
        return self.success_url


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('posts_list_url')
    

class PostsList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    slug_field = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['post_mutable'] = True
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('user_login_url')
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        print('='*20, self.object.author)
        print('='*20, self.object.author.get_full_name())
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = reverse_lazy('user_login_url')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    # success_url = reverse_lazy('posts_list_url')
    success_url = '/'
    login_url = reverse_lazy('user_login_url')

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if self.request.user != post.author:
            self.handle_no_permission()
        return super().delete(self, request, *args, **kwargs)


class TagList(ListView):
    model = Tag
    context_object_name = 'tags'


class TagDetail(DetailView):
    model = Tag
    context_object_name = 'tag'
    slug_field = 'slug'


class TagCreate(LoginRequiredMixin, CreateView):
    form_class = TagForm
    template_name = 'blog/tag_form.html'
    login_url = reverse_lazy('user_login_url')


class AuthorPosts(ListView):
    template_name = 'blog/author_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(author__username=self.kwargs['name'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {'author': User.objects.get(username=self.kwargs['name'])}
        return super().get_context_data(**context)


class AuthorList(ListView):
    template_name = 'blog/authors.html'
    context_object_name = 'authors'

    def get_queryset(self):
        authors = Post.objects.values_list('author', flat=True).distinct().order_by()
        return User.objects.filter(pk__in=authors)
