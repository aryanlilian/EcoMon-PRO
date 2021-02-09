from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment
from users.models import User


class BaseTest(TestCase):

    def setUp(self):
        self.blog_url = reverse('blog')
        self.tag_url = reverse('tag', args=['test'])
        self.post_url = reverse('post', args=['test-post'])
        self.add_post_url = reverse('add-post')
        self.user = User.objects.create(
            username='testuser',
            email='test@test.com',
            first_name='test',
            last_name='test',
            password='test'
        )
        self.post = {
            'title' : 'test post',
            'content' : 'testing content post',
            'category' : 'FAMILY',
            'tags' : ''
        }
        self.empty_title_post = {
            'title' : '',
            'content' : 'testing content post',
            'category' : 'FAMILY',
            'tags' : 'test'
        }
        self.empty_content_post = {
            'title' : 'test post',
            'content' : '',
            'category' : 'FAMILY',
            'tags' : 'test'
        }
        return super().setUp()

class TestBlogViews(BaseTest):

    def test_blog_list_view_GET(self):
        response = self.client.get(self.blog_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')


class TestTaggetPostViews(BaseTest):

    def test_tagged_post_list_view_GET(self):
        post = Post.objects.create(author=self.user, title=self.post['title'], content=self.post['content'], category=self.post['category'])
        post.tags.add('test')
        response = self.client.get(self.tag_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')


class TestPostDetailViews(BaseTest):

    def test_post_detail_view_GET(self):
        post = Post.objects.create(author=self.user, title=self.post['title'], content=self.post['content'], category=self.post['category'])
        response = self.client.get(self.post_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post.html')


class TestPostCreateViews(BaseTest):

    # def test_post_create_view_GET(self):
    #     response = self.client.get(self.add_post_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/add_post.html')
    #
    # def test_post_create_view_POST_success(self):
    #     response = self.client.post(self.add_post_url, self.post, author=self.user, follow=True) # make sure your url is correct too btw that could also be the issue
    #     self.assertEquals(response.status_code, 302)
    #
    # def test_post_create_view_POST_taken_title(self):
    #     self.client.post(self.add_post_url, self.post, author=self.user)
    #     response = self.client.post(self.add_post_url, self.post, author=self.user)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_post_create_view_POST_empty_title(self):
    #     response = self.client.post(self.add_post_url, self.empty_title_post, author=self.user, format='text/html')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_post_create_view_POST_empty_content(self):
    #     response = self.client.post(self.add_post_url, self.empty_content_post, author=self.user, format='text/html')
    #     self.assertEqual(response.status_code, 200)
