from django.test import TestCase
from ..models import Subscription
from django.shortcuts import resolve_url as r


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(name='Marcos Rogerio',
                                               cpf='03388885629',
                                               email='mrpsousa@outlook.com',
                                               phone='71-99250-0187')

        self.response = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.response, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        self.assertContains(self.response, self.obj.name)
        self.assertContains(self.response, self.obj.cpf)
        self.assertContains(self.response, self.obj.email)
        self.assertContains(self.response, self.obj.phone)


class SubscriptionDetailNotFound(TestCase):
    def test_not_foud(self):
        response = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, response.status_code)
