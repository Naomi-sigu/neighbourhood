from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.hood = Neighbourhood(neighbourhood='umoja', occupants=23)

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighbourhood))

   
   
  