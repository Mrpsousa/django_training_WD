# from django.http import response
from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
# from project.subscriptions.forms import SubscriptionForm


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Marcos Rogerio', cpf='03388885629',
                    email='mrpsousa@outlook.com', phone='71-99250-0187')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        """ TODO """
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        """ TODO """
        expect = 'mrpsousa@outlook.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        """ TODO """
        expect = ['mrpsousa@outlook.com', 'mrpsousa@outlook.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        """ TODO """
        # contents = ['Marcos Rogerio',
        #             '03388885629'
        #             'mrpsousa@outlook.com'
        #             '71-99250-0187']
        # for content in contents:
        #     with self.subTest():
        #         self.assertIn(content, self.email.body)

        self.assertIn('Marcos Rogerio', self.email.body)
        self.assertIn('03388885629', self.email.body)
        self.assertIn('mrpsousa@outlook.com', self.email.body)
        self.assertIn('71-99250-0187', self.email.body)
