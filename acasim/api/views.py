from rest_framework.views import APIView
from django.conf import settings
import requests
import base64

from accounts.forms import SignInForm


class LoginApiView(APIView):
    def post(self, request):
        url = f"{settings.HOST}/o/token/"
        form = SignInForm(request, data=request.data)
        if form.is_valid():
            user = form.get_user()
            print(user)
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
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()

