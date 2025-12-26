from django.test import TestCase
from ..models import Section

class SectionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Section.objects.create(title='Main', slug='main')
        

    def setUp(self):
        print('setUp вызывается перед каждым тестом')

    def tearDown(self):
        print('tearDown вызывается послекаждого теста')

    def test_title_max_length(self):
        obj = Section.objects.get(id=1)
        max_length = obj._meta.get_field('title').max_length
        self.assertEqual(max_length,70)

    def test_title_help_text(self):
        obj = Section.objects.get(id=1)
        help_text = obj._meta.get_field('title').help_text
        self.assertEqual(help_text,'Тут надо ввести название раздела')

    def test_title_unique(self):
        obj = Section.objects.get(id=1)
        unique = obj._meta.get_field('title').unique
        self.assertTrue(unique)


    