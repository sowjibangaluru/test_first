from django.test import TestCase
import requests

# Create your tests here.
Base_Url='http://127.0.0.1:8000/'
ENDPOINT='api'
res=requests.get(Base_Url+ENDPOINT)
data=res.json()
print(data)

