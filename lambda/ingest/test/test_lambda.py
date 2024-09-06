import unittest
import requests

URL = "http://lambda_ingest:8080/2015-03-31/functions/function/invocations"

# Función que realiza una solicitud POST
def post_request(url, data):
    response = requests.post(url, json=data)
    return response


# Clase de prueba
class TestPostRequest(unittest.TestCase):
    
    def test_post_request_no_download(self):
        # Datos ficticios para enviar en el POST
        data = {"download": False}        
        # Llamada a la función que hace el POST
        response = post_request(URL, data)
        # Verificar que el código de estado es 200
        self.assertEqual(response.status_code, 200)


    # def test_post_request_empty(self):
    #     # Datos ficticios para enviar en el POST
    #     data = {}        
    #     # Llamada a la función que hace el POST
    #     response = post_request(URL, data)
    #     # Verificar que el código de estado es 200
    #     self.assertEqual(response.status_code, 402)


    def test_post_request_download(self):
        # Datos ficticios para enviar en el POST
        data = {"download": True}        
        # Llamada a la función que hace el POST
        response = post_request(URL, data)
        # Verificar que el código de estado es 200
        self.assertEqual(response.status_code, 200)




# Ejecución de las pruebas
if __name__ == '__main__':
    unittest.main()
