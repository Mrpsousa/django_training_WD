from django.test import TestCase
from project.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
       self.form = SubscriptionForm()

    def test_has_fields(self):
        """ Form must have 4 fields."""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_cpf_is_digit(self):
        """ CPF must only accpet digits"""
        form = self.make_validated_form(cpf='ABCD1234567')

        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """ CPF must 11 digits"""
        form = self.make_validated_form(cpf='1234')

        self.assertFormErrorCode(form,'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Marcos Rogerio', cpf='13258885629',
                    email='mrpsousa@outlook.com', phone='71-99250-0187')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
