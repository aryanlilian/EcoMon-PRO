from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (
    BlogListView,
    TaggedPostListView,
    PostDetailView,
    PostCreateView
)


class TestUrls(SimpleTestCase):

    def test_blog_url_resolves(self):
        url = reverse('blog')
        self.assertEquals(resolve(url).func.view_class, BlogListView)

    def test_tag_url_resolves(self):
        url = reverse('tag', args=['test-slug'])
        self.assertEquals(resolve(url).func.view_class, TaggedPostListView)

    def test_post_url_resolves(self):
        url = reverse('post', args=['test-slug'])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_add_post_url_resolves(self):
        url = reverse('add-post')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)
