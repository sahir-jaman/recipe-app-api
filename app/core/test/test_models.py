
from decimal import Decimal
from core import models
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ test models """

    def test_create_user_with_successful(self):
        """ Test creating a user with an email is successful """

        email = 'test@example.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """" test email is normalized for new users """
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.COM', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@EXAMPLE.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        # test that creating a user without email raising a valueError
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_creating_superuser(self):
        # test creating a superuser
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )
        # self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user = user,
            title = 'sample recipe name',
            description = 'sample des',
            time_minutes = 5,
            price= Decimal('5.50')
        )
        self.assertEqual(str(recipe), recipe.title)
