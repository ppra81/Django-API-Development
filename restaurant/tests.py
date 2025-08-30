from django.test import TestCase
from rest_framework.test import APIClient
from .models import MenuItem, Booking
from django.contrib.auth.models import User

class MenuItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        MenuItem.objects.create(name='Pizza', description='Cheesy', price=10.99, category='Main')

    def test_get_menu_items(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

class BookingTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_booking(self):
        data = {'user': self.user.id, 'table_number': 1, 'date': '2025-09-01', 'time': '18:00', 'guests': 4}
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, 201)