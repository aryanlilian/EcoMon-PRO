from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Post, Comment
from users.models import Profile
from taggit.models import Tag
from .forms import PostCreateForm, CommentUpdateForm
from .filters import PostFilterForm
from common.mixins import IsSuperuserOrStaffMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from common.constants import template_titles, help_texts, messages_text, newsletter_texts
from home.models import Newsletter
from django.contrib import messages
from django.core.mail import send_mail
from common.utils import uidb_token_generator
from django.conf import settings
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 2
    filterset_class = PostFilterForm
    post_search_title = None

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        email = request.POST.get('newsletter_email')
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, messages_text['email_exists'])
        else:
            fin, newsletter_email_content = open('common/emails/newsletter_welcome.txt', 'rt'), ''
            unsubsribe_url = uidb_token_generator('unsubsribe', request, email)
            for line in fin:
                newsletter_email_content += line.replace('user_email', email)
            newsletter_email_content += '\n' + unsubsribe_url
            try:
                subject = newsletter_texts['subject']
                send_mail(
                    subject,
                    newsletter_email_content,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False
                )
                Newsletter.objects.create(email=email)
                messages.success(request, messages_text['email_subscribed'])
            except:
                messages.warning(request, messages_text['fail_sent_email'])
            return redirect('blog')
        return render(request, self.template_name, context)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.post_search_title = self.filterset_class(self.request.GET, queryset=queryset)
        return self.post_search_title.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_search_title'] = self.post_search_title
        context['recent_posts'] = Post.objects.order_by('-published_date')[:3]
        context['banner_page_title'] = template_titles['blog_title']
        context['page_location'] = template_titles['blog_path']
        context['title'] = template_titles['blog_title']
        context['tags'] = Post.tags.most_common()[:8]
        return context


class TaggedPostListView(BlogListView):

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        email = request.POST.get('newsletter_email')
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, messages_text['email_exists'])
        else:
            fin, newsletter_email_content = open('common/emails/newsletter_welcome.txt', 'rt'), ''
            unsubsribe_url = uidb_token_generator('unsubsribe', request, email)
            for line in fin:
                newsletter_email_content += line.replace('user_email', email)
            newsletter_email_content += '\n' + unsubsribe_url
            try:
                subject = newsletter_texts['subject']
                send_mail(
                    subject,
                    newsletter_email_content,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False
                )
                Newsletter.objects.create(email=email)
                messages.success(request, messages_text['email_subscribed'])
            except:
                messages.warning(request, messages_text['fail_sent_email'])
            return redirect('tag', kwargs['slug'])
        return render(request, self.template_name, context)

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        tagged_post = Post.objects.filter(tags=tag)
        self.post_search_title = self.filterset_class(self.request.GET, queryset=tagged_post)
        return self.post_search_title.qs.distinct()


class PostDetailView(View):
    template_name = 'blog/post.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        content, replied_comment = request.POST.get('commentContent'), None
        if content:
            comment_id = request.POST.get('commentId')
            post = Post.objects.get(slug=kwargs['slug'])
            if comment_id:
                replied_comment = Comment.objects.get(id=comment_id)
            Comment.objects.create(
                author=request.user,
                post=post,
                reply=replied_comment,
                content=content
            )
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        post = Post.objects.get(slug=kwargs['slug'])
        try:
            context['previous_post'] = Post.objects.get(id=post.id - 1)
        except:
            context['previous_post_none'] = template_titles['no_previous_post']
        try:
            context['next_post'] = Post.objects.get(id=post.id + 1)
        except:
            context['next_post_none'] = template_titles['no_next_post']
        context['banner_page_title'] = post.title
        context['title'] = template_titles['post_title']
        context['page_location'] = template_titles['post_path']
        context['post'] = post
        context['comments'] = Comment.objects.filter(post=post, reply=None)
        context['author_description'] = Profile.objects.get(user=post.author).description
        context['comment_content_help_text'] = help_texts['any_character']
        return context



class PostCreateView(LoginRequiredMixin, IsSuperuserOrStaffMixin, CreateView):
    template_name = 'blog/add_post.html'
    form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_page_title'] = template_titles['post_create']
        context['title'] = template_titles['post_title']
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_page_title'] = template_titles['post_update']
        context['title'] = template_titles['post_title']
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'users/post.html'
    success_url = reverse_lazy('blog')

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentUpdateForm
    template_name = 'blog/update_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'users/post.html'
    success_url = reverse_lazy('blog')

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'slug': self.get_object().post.slug})

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(author=self.request.user)
