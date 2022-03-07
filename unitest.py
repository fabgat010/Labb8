import unittest
from main import *

class TestSyntaxKoll(unittest.TestCase):
    #Ska fungera
    def testa_H2(self):
        self.assertEqual(tryexcept("H2"), 'Formeln är syntaktiskt korrekt')
    def testing_P21(self):
        self.assertEqual(tryexcept("P21"), "Formeln är syntaktiskt korrekt")
    def testa_Ag3(self):
        self.assertEqual(tryexcept("Ag3"), "Formeln är syntaktiskt korrekt")
    def testa_Xx5(self):
        self.assertEqual(tryexcept("Xx5"), 'Formeln är syntaktiskt korrekt')
    def testa_H10100(self):
        self.assertEqual(tryexcept("H10100"), 'Formeln är syntaktiskt korrekt')

    #Ska inte fungera
    def testa_fel_grupp_a(self):
        self.assertEqual(tryexcept("a"), "Saknad stor bokstav vid radslutet a")
    def testa_fel_grup_cr12(self):
        self.assertEqual(tryexcept("cr12"), "Saknad stor bokstav vid radslutet cr12")
    def testa_fel_grupp_8(self):
        self.assertEqual(tryexcept("8"), "Saknad stor bokstav vid radslutet 8")
    def testa_fel_grupp_Cr0(self):
        self.assertEqual(tryexcept("Cr0"), "För litet tal vid radslutet ")
    def testa_fel_grupp_Pb1(self):
        self.assertEqual(tryexcept("Pb1"), 'För litet tal vid radslutet ') #ett mellanslag på slutet
    def testa_fel_grupp_H01011(self):
        self.assertEqual(tryexcept("H01011"), "För litet tal vid radslutet 1011")
    


if __name__ == '__main__':
    unittest.main()