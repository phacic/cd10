from django.test import TestCase
import pprint
import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from cd10 import models, serializers


class DiagnosisViewsTest(APITestCase):

    def setUp(self) -> None:
        self.cat1 = models.Category.objects.create(code='A00', title='Cholera')

        code = 0
        full_code = 'A000'
        abbr_desc = 'Cholera due to Vibrio cholerae 01, biovar cholerae'
        desc = 'Cholera due to Vibrio cholerae 01, biovar cholerae'

        self.diag1 = models.Diagnosis.objects.create(category=self.cat1, code=code, full_code=full_code,
                                                     abbreviated_description=abbr_desc, full_description=desc)

    def test_get_diagnosis_with_non_existing_id(self):
        """ should return 404 for non existing diagnosis """

        url = reverse('cd10:diagnosis-detail', args=[22])

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 404)

    def test_get_diagnosis_with_existing_id(self):
        """ should return diagnosis """

        url = reverse('cd10:diagnosis-detail', args=[self.diag1.id])

        resp = self.client.get(url)

        # should not return with 404
        self.assertNotEqual(resp.status_code, 404)

        # should contain
        self.assertContains(resp, 'full_description')

        # category_detail object should be present
        self.assertContains(resp, 'category_detail')

    def test_list_diagnosis(self):
        """ ensure diagnosis can be listed """
        url = reverse('cd10:diagnosis-list')
        resp = self.client.get(url)

        # status code should be 200
        self.assertEqual(resp.status_code, 200)

        # resp should contain item in an array
        self.assertEqual(len(resp.data), 1)

        # single data should look like
        self.assertDictEqual(resp.data[0], serializers.DiagnosisSerializer(self.diag1).data)

    def test_create_diagnosis(self):
        """ ensure diagnosis can be created through the endpoint """

        url = reverse('cd10:diagnosis-list')
        code1 = 1
        full_code1 = 'A001'
        abbr_desc1 = 'Cholera due to Vibrio cholerae 01, biovar eltor'
        desc1 = 'Cholera due to Vibrio cholerae 01, biovar eltor'

        data = {'category': self.cat1.id, 'code': code1, 'full_code': full_code1,
                'abbreviated_description': abbr_desc1, 'full_description': desc1
                }

        resp = self.client.post(url, data, format='json')

        # status code should be 201
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        # category id should be 1
        self.assertEqual(resp.data['category'], self.cat1.id)

        # diagnosis should be two
        self.assertEqual(models.Diagnosis.objects.count(), 2)

    def test_update_diagnosis(self):
        """ ensure diagnosis can be updated """

        url = reverse('cd10:diagnosis-detail', args=[self.diag1.id])
        data = {'code': '1', "full_code": "A001"}

        resp = self.client.patch(url, data, format='json')

        # should respond with status code 200
        self.assertEqual(resp.status_code, 200)

        # return full code should be what was submitted
        self.assertEqual(resp.data['full_code'], "A001")

        # changes should reflect in database
        self.assertEqual(models.Diagnosis.objects.first().full_code, "A001")

    def test_delete_diagnosis(self):
        """ ensure a diagnosis can be deleted """
        url = reverse('cd10:diagnosis-detail', args=[self.diag1.id])

        resp = self.client.delete(url)

        # status code should be 204
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

        # item should be really be removed from database
        self.assertEqual(models.Diagnosis.objects.filter(id=self.cat1.id).count(), 0)


class CategoryViewsTest(APITestCase):

    # def setUp(self) -> None:
    #     self.cat1 = models.Category.objects.create()

    def test_create_category(self):
        """ ensure new category can be created """

        url = reverse('cd10:category-list')
        data = {'code': 'A00', 'title': 'Cholera'}
        resp = self.client.post(url, data, format='json')

        # status code should be 201
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        # categories should have one item
        self.assertEqual(models.Category.objects.count(), 1)

        # and that item should be Cholera
        self.assertEqual(models.Category.objects.first().title, 'Cholera')

    def test_update_category(self):
        pass

    def test_delete_category(self):
        pass
