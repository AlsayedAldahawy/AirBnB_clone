#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBase
from models.user import User


class test_User(TestBase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

        new.first_name = "Alsayed"
        self.assertEqual(new.first_name, "Alsayed")

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

        new.last_name = "Aldahawy"
        self.assertEqual(new.last_name, "Aldahawy")

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

        new.email = "abcd@efg.com"
        self.assertEqual(new.email, "abcd@efg.com")

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

        new.password = "12345"
        self.assertEqual(new.password, "12345")
