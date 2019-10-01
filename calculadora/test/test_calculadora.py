from django.test import TestCase
from calculadora import views


class CalculadoraTests(TestCase):

    def test_soma(self):
        self.assertEqual(views.soma(2, 2), 4)
