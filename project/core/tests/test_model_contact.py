from django.core.exceptions import ValidationError
from django.test import TestCase
from project.core.models import Contact, Speaker
from django.shortcuts import resolve_url as r


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic',
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='henrique@bastos.net')
        self.assertTrue(Contact.objects.exists())

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE, value='71-992200187')
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """ Contact king should be limited to E or P """
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='henrique@bastos.net')
        self.assertEqual('henrique@bastos.net', str(contact))