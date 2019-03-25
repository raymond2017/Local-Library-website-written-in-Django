from django.test import TestCase

# Create your tests here.
from catalog.models import Author


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big', last_name='Bob')

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        first_name_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(first_name_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        last_name_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(last_name_label, 'last name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        date_of_death_label = author._meta.get_field(
            'date_of_death').verbose_name
        self.assertEqual(date_of_death_label, 'died')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        date_of_birth_label = author._meta.get_field(
            'date_of_birth').verbose_name
        self.assertEqual(date_of_birth_label, 'date of birth')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        name = '{}, {}'.format(author.last_name, author.first_name)
        self.assertEqual(name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')
