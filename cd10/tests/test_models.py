from django.test import TestCase

from cd10.models import Category, Diagnosis


class CategoryModelTests(TestCase):

    def test_create_category(self):
        """ category should be created with code, title, created and updated fields"""
        new_category = Category(code='A00', title='Cholera')
        new_category.save()

        c = Category.objects.first()
        self.assertEqual(c.code, 'A00')
        self.assertEqual(c.title, 'Cholera')

        # should have created and updated field though they were not provided
        self.assertIsNotNone(c.created)
        self.assertIsNotNone(c.updated)

    def test_create_multiple_categories(self):
        """ categories should be created """
        cat1 = Category(code='A00', title='Cholera')
        cat2 = Category(code='A010', title='Typhoid fever')

        Category.objects.bulk_create([cat1, cat2])

        cats = Category.objects.all()
        self.assertEqual(cats.count(), 2)


class DiagnosisModelTests(TestCase):

    def setUp(self) -> None:
        self.cat1 = Category.objects.create(code='A00', title='Cholera')

    def test_create_diagnosis(self):
        """ diagnosis should be created """

        code = 0
        full_code = 'A000'
        abbr_desc = 'Cholera due to Vibrio cholerae 01, biovar cholerae'
        desc = 'Cholera due to Vibrio cholerae 01, biovar cholerae'

        Diagnosis.objects.create(category=self.cat1, code=code, full_code=full_code,
                                 abbreviated_description=abbr_desc, full_description=desc)

        diag = Diagnosis.objects.first()

        self.assertEqual(diag.category_id, self.cat1.id)
        self.assertIsNotNone(diag.created)
        self.assertIsNotNone(diag.updated)

    def test_create_multiple_diagnosis(self):
        """ multiple should be created """

        code1 = 0
        full_code1 = 'A000'
        abbr_desc1 = 'Cholera due to Vibrio cholerae 01, biovar cholerae'
        desc1 = 'Cholera due to Vibrio cholerae 01, biovar cholerae'

        code2 = 1
        full_code2 = 'A001'
        abbr_desc2 = 'Cholera due to Vibrio cholerae 01, biovar eltor'
        desc2 = 'Cholera due to Vibrio cholerae 01, biovar eltor'

        Diagnosis.objects.bulk_create([
            Diagnosis(category=self.cat1, code=code1, full_code=full_code1, abbreviated_description=abbr_desc1,
                      full_description=desc1),
            Diagnosis(category=self.cat1, code=code2, full_code=full_code2, abbreviated_description=abbr_desc2,
                      full_description=desc2),
        ])

        diagnosis = Diagnosis.objects.all()
        self.assertEqual(diagnosis.count(), 2)
