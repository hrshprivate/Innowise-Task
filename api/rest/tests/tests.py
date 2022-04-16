from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from rest.models import Ticket
from rest.serializers import TicketSerializer


class UserTest(TestCase):
    def setUp(self):
        # Новый пользователь штатными методами
        user = User.objects.create_user(
            username='Test',
            email='test@mail.ru',
            password='password1337'
        )

    def test_user(self):
        user = User.objects.get(username='Test')
        db_table = user._meta.db_table
        self.assertEquals(db_table, 'auth_user')


class TicketTest(APITestCase):
    def test_api(self):
        ticket_1 = Ticket.objects.create(title='Test', content='TestContent')
        ticket_2 = Ticket.objects.create(title='Test2', content='TestContent2')
        url = reverse('list')
        response = self.client.get(url)
        serializer_data = TicketSerializer([ticket_1, ticket_2], many=True).data
        self.assertEquals(serializer_data, response.data)


class TestJwt(APITestCase):
    def test_jwt(self):
        user = User.objects.create_user(
            username='Test',
            email='test@mail.ru',
            password='password1337'
                 )
        self.client = APIClient()
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {refresh.access_token}')
        return self.client
