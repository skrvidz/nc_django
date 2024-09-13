from django.test import TestCase
from .models import OperationalVariable

class OperationalVariableTestCase(TestCase):
    def setUp(self):
        OperationalVariable.objects.create(name="Pressure", value=101.3)

    def test_operational_variable(self):
        var = OperationalVariable.objects.get(name="Pressure")
        self.assertEqual(var.value, 101.3)
