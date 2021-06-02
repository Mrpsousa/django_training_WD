from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """ GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """  Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        """ ALGO """
        self.assertContains(self.response, 'href="/inscricao/"')

    def test_speakers(self):
        """ Must show keynote speakers"""
        self.assertContains(self.response, 'Grace Hopper')
        self.assertContains(self.response, 'http://hbn.link/hopper-pic')
        self.assertContains(self.response, 'Alan Turing')
        self.assertContains(self.response, 'http://hbn.link/turing-pic')

    def test_speakers_link(self):
        expected = 'href="{}#speakers'.format(r('home'))
        self.assertContains(self.response, expected)