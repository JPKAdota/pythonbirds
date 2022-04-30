from unittest import TestCase


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidad)
    def tes_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.acelerar)