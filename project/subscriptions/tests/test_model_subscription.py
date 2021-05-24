from django.test import TestCase
from ..models import Subscription
import datetime


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Rogerio',
            cpf='12345678901',
            email='algo@gmail.com',
            phone='71-982309876'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscripton must have an auto created_at attribute """
        self.assertIsInstance(self.obj.created_at, datetime.datetime)

    def test_srt(self):
        self.assertEqual('Rogerio', str(self.obj))

    def test_paid_default_to_False(self):
        """ By Default paid must be False"""
        self.assertEqual(False, self.obj.paid)