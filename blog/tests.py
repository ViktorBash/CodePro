from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
# Create your tests here.

class PostTestCase(TestCase):
    def setUp(self):
        User1 = User.objects.create_user(username="Jacob", email="jacob@google.com", password="Password1234")
        User2 = User.objects.create_user(username="Robby", email="baseballover@gmail.com", password="Kirk09")
        Post.objects.create(title="My First Post", content="Wow! I love learning Python so much that I started a blog because of it!", author=User1)
        Post.objects.create(title="Experienced Blogger", content="This is my second post, and now I am an experienced blogger.", author=User2)

    def test_posts(self):
        # Testing out our Post models
        post1 = Post.objects.get(title="My First Post")
        post2 = Post.objects.get(title="Experienced Blogger")
        User1 = User.objects.get(username="Jacob")
        User2 = User.objects.get(username="Robby")
        self.assertEqual(User1.email, "jacob@google.com")
        self.assertEqual(User2.username, "Robby")
        self.assertEqual(post1.author, User1)
        print("Test")
