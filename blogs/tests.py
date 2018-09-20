from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your tests here.


def testAuth():
    user = authenticate(username='admin', password='abc123')
    if user is None:
        print('user not auth')
    else:
        print('user had auth')



if __name__ == '__main__':
    testAuth()