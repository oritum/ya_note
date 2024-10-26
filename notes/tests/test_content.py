# from datetime import datetime, timedelta
# from django.utils import timezone
from django.contrib.auth import get_user_model
from django.test import TestCase
from notes.models import Note
# from news.forms import CommentForm

User = get_user_model()


class TestSlug(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='oritum')
        cls.note = Note.objects.create(
            text='text', title='привет', author=cls.author
        )

    def test_slug_translit(self):
        self.assertEqual(self.note.slug, 'privet')
