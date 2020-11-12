# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.test import TestCase    #Testear cosas de la BD
import unittest                     #Testear normal

# Create your tests here.

class NumberTestCase(TestCase):

  #Ojo, Deben llevar test_ para que funcione      
  def test_number_sum(self):    
    self.assertEqual("SI", "NO")
