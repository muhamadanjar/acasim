from typing import Any
from django.contrib.auth.forms import AuthenticationForm


class SignInForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)	
		self.fields["username"].label = "Username"
		self.fields["password"].label = "Password"