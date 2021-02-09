from django.db import models
from users.models import User
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from django.urls import reverse

class Post(models.Model):

    class PostCategory(models.TextChoices):
        FAMILY = 'FAMILY', _('Family')
        BUSSINESS = 'BUSSINESS', _('Bussiness')
        MWRKETING = 'MARKETING', _('Marketing')
        SPENDINGS = 'SPENDINGS', _('Spendings')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=200, unique=True)
    content = models.TextField(_('Content'))
    category = models.CharField(_('Category'), max_length=9, choices=PostCategory.choices, default=PostCategory.BUSSINESS)
    full_image = models.ImageField(_('Full Image'), default='full_blog_image.jpg', upload_to='blog_pics')
    medium_image = models.ImageField(_('Medium Image'), default='medium_blog_image.jpg', upload_to='blog_pics')
    small_image = models.ImageField(_('Small Image'), default='small_blog_image.jpg', upload_to='blog_pics')
    slug = models.SlugField(_('Slug'), max_length=200, blank=True, null=False, unique=True)
    tags = TaggableManager(_('Tags'))
    published_date = models.DateTimeField(_('Published Date/Time'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def comments_count(self):
        return self.comments.count()

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug' : self.slug})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    content = models.TextField(_('Content'))
    posted_date = models.DateTimeField(_('Posted Date/Time'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)

    def __str__(self):
        return f'{self.author.username} - {self.post.title}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug' : self.post.slug})
