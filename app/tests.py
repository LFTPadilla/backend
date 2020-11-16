# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.test import TestCase    #Testear cosas de la BD
import unittest                     #Testear normal
import requests_mock
import requests
from .views import GetRequirement
from authentication.views import login_view
# Create your tests here.

class NumberTestCase(TestCase):

  #Ojo, Deben llevar test_ para que funcione      
  def test_login_page(self):
    with open("app/issues_one_page.json", "r") as issues_file:
        mock_response = issues_file.read()
 
    expected_result = {'Success':'false',"User":'null'}
 
    with requests_mock.Mocker() as m:
        m.post('http://localhost:8000/auth/login', json={'login':'felipe','password':'12345678'})
        
        view = login_view(m)
        #result = view.dispatch(requests.get('http://localhost:8000/auth/login').text, service='remote_service')
        print("request",view)
    return req
    #self.assertEqual(expected_result, response)

