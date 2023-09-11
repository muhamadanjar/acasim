from rest_framework.views import APIView
import requests
import base64


class LoginApiView(APIView):
    def post(self, request):
        url = "http://localhost:8000/o/token/"
        credentials = "{}:{}".format("client_id", "secret")
        basic_auth = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
        headers = {
            "Authorization": f"Basic {basic_auth}"
        }
        data = {
            "grant_type": "password",
            "username": "admin",
            "password": "password"
        }
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            return response.json()

