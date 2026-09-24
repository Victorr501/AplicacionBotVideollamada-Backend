import request

class HttpClient:
    def __init__(self):
        self.session = request.Session()

        self.session.headers.update({
            "Content-Type": "application/json"
            })

    def post(self, url: str, data: dict, custom_headers: dict = None):
        """
        Ejecuta un POST fusionando los headers globales con los específicos de esta petición.
        """
        headers = custom_headers if custom_headers else {}

        response = self.session.post(url, json = data, headers = headers)
        response.raise_for_status()
        return response

    # Aqui añadimos mas metodos de get(), etc

http_client = HttpClient()