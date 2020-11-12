# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.test import TestCase

# Create your tests here.

class NumberTestCase(TestCase):
  def simple_test(self):    
    self.assertEqual(4,4) 
