# from django.http import response
from django.core import mail
from django.test import TestCase
from project.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """GET /inscricao/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(
            self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'],
                                 list(form.fields))


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Marcos Rogerio', cpf='03388885629',
                    email='urameshi.uba@gmail.com', phone='71-99250-0187')
        self.response = self.client.post('/inscricao/', data)
        
    def test_post(self):
        """Valid POST should redirect to /inscicao/"""
        self.assertEqual(302, self.response.status_code)
    
    def test_send_subscribe_email(self):
        """ TODO """
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        """ TODO """
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self):
        """ TODO """
        email = mail.outbox[0]
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        """ TODO """
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br', 'urameshi.uba@gmail.com']

        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        """ TODO """
        email = mail.outbox[0]

        self.assertIn('Marcos Rogerio', email.body)
        self.assertIn('03388885629', email.body)
        self.assertIn('urameshi.uba@gmail.com', email.body)
        self.assertIn('71-99250-0187', email.body)