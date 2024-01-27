from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class ProductListTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('ProductList')
        self.token_url = reverse('token_obtain_pair')
        # JWT auth
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.auth_client = APIClient()
        response = self.client.post(self.token_url, {
                                    'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.token = response.data['access']

    def test_unauthorized_get_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_product_creation(self):
        sample_product = {
            "name": "eggs",
            "description": "A single carton of eggs",
            "price": 11.5
        }
        response = self.client.post(self.url, sample_product)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorized_get_products(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_authorized_product_creation(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        sample_product = {
            "name": "eggs",
            "description": "A single carton of eggs",
            "price": 11.5
        }
        response = self.client.post(self.url, sample_product, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_authorized_get_products(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        sample_product = {
            "name": "eggs",
            "description": "A single carton of eggs",
            "price": 11.5
        }
        response = self.client.post(self.url, sample_product, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.get(self.url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data),0)
        
    
class ProductDetailTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('ProductList')
        self.detail_url = reverse('ProductDetail', kwargs={'pk': 1})
        self.token_url = reverse('token_obtain_pair')
        # JWT auth
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.auth_client = APIClient()
        response = self.client.post(self.token_url, {
                                    'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.token = response.data['access']

    def test_unauthorized_get_product(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_product_update(self):
        sample_product = {
            "name": "rare eggs",
            "description": "An expensive carton of eggs",
            "price": 20
        }
        response = self.client.post(self.detail_url, sample_product)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_unauthorized_product_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorized_not_found_product(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.get(self.detail_url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_authorized_get_product(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        sample_product = {
            "name": "eggs",
            "description": "A single carton of eggs",
            "price": 11.5
        }
        response = self.client.post(self.url, sample_product, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.get(self.detail_url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
        
    def test_authorized_product_update(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        sample_product = {
            "name": "eggs",
            "description": "A single carton of eggs",
            "price": 11.5
        }
        response = self.client.post(self.url, sample_product, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        updated_product = {
            "name": "rare eggs",
            "description": "An expensive carton of eggs",
            "price": 20
        }
        response = self.client.put(self.detail_url, updated_product, headers=headers)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "rare eggs")
        self.assertNotEqual(response.data['created_at'], response.data['updated_at'])
        
    def test_authorized_product_delete(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        sample_product = {
            "name": "eggs",
            "description": "A single carton of eggs",
            "price": 11.5
        }
        response = self.client.post(self.url, sample_product, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.delete(self.detail_url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        response = self.client.get(self.detail_url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)