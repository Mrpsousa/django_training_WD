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

    def test_name_must_be_capitalized(self):
        """ Name must be capitalized"""
        # MARCOS rogerio -> Marcos Rogerio
        form = self.make_validated_form(name='MARCOS rogerio')
        self.assertEqual('Marcos Rogerio', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """ Email is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """ Email is optional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """ Email and Phone are optional, but one must be informed."""
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

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
