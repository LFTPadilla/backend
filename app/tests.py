# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.test import TestCase    #Testear cosas de la BD
import unittest                     #Testear normal
import requests_mock
# Create your tests here.

class NumberTestCase(TestCase):

  #Ojo, Deben llevar test_ para que funcione      
  def test_get_updated_issues_one_page(self):
    with open("app/issues_one_page.json", "r") as issues_file:
        mock_response = issues_file.read()
 
    expected_result = {'Success':'false',"User":'null'}
 
    with requests_mock.Mocker() as m:
        m.post('/auth/login', json={'login':'felipe','password':'12345678'})
        print(m.)
        #response = jiratimereport.get_updated_issues("https://jira_url", "user_name", "api_token",  "MYB", "2020-01-10", "2020-01-20", "")
    self.assertEqual(expected_result, response)
