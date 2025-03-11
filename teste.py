import requests
import unittest

class TestStringMethods(unittest.TestCase):


    def test_000_alunos_retorna_lista(self):
        r = requests.get('http://127.0.0.1:5000/')

        #o status code foi pagina nao encontrada?
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina / no seu server")

        try:
            obj_retornado = r.json()
            #r.json() é o jeito da biblioteca requests
            #de pegar o arquivo que veio e transformar
            #em lista ou dicionario.
            #Vou dar erro se isso nao for possivel
        except:
            self.fail("queria um json mas voce retornou outra coisa")

        #no caso, tem que ser uma lista
        self.assertEqual(type(obj_retornado),type([]))  


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()