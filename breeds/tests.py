from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Breeds

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_breed = Breeds.objects.create(
            purchaser = testuser1,
            name = 'Airedale Terrier',
            description = 'His size, strength, and unflagging spirit have earned the Airedale Terrier the nickname “The King of Terriers.',
            height = 23,
            weight = 60
        )
        test_breed.save()

    def test_blog_content(self):
        Breed = Breeds.objects.get(id=1)
        actual_purchaser = str(Breed.purchaser)
        actual_name = str(Breed.name)
        actual_description = str(Breed.description)
        actual_height = str(Breed.height)
        actual_weight = str(Breed.weight)
        self.assertEqual(actual_purchaser, 'testuser1')
        self.assertEqual(actual_name, 'Airedale Terrier')
        self.assertEqual(actual_description, 'His size, strength, and unflagging spirit have earned the Airedale Terrier the nickname “The King of Terriers.')
        self.assertEqual(actual_height, '23')
        self.assertEqual(actual_weight, '60')
