#!/usr/bin/python3
""" test console """
import uuid
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class test_console(unittest.TestCase):
    """ class to test console """

    ##########
    # create #
    ##########

    def test_create_user(self):
        """ test create user """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        test_id = f.getvalue()
        try:
            uuid.UUID(test_id.strip())
            test = True
        except:
            test = False
        self.assertTrue(test)

    def test_create_base_model(self):
        """ test create user """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        test_id = f.getvalue()
        try:
            uuid.UUID(test_id.strip())
            test = True
        except:
            test = False
        self.assertTrue(test)

    def test_create_no_class(self):
        """ test create without class name """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_create_wrong_class(self):
        """ test create with class that doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    ########
    # show #
    ########

    def test_show(self):
        """ test show """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_id = (f.getvalue()).strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(test_id))
        test = True
        if "[BaseModel]" not in f.getvalue():
            test = False
        if test_id not in f.getvalue():
            pass
            test = False
        self.assertTrue(test)

    def test_show_no_class(self):
        """ test show without class name """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_show_wrong_class(self):
        """ test show with class that doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel 1234-1234-1234")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_no_id(self):
        """ test show without id """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_show_wrong_id(self):
        """ test show with id that doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234-1234-1234")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    ###########
    # destroy #
    ###########

    def test_destroy(self):
        """ test destroy """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        test_id = (f.getvalue()).strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(test_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(test_id))
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy_no_class(self):
        """ test destroy without class """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_destroy_no_id(self):
        """ test detroy without id """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_destroy_wrong_class(self):
        """ test destroy with class that doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyClass 1234-1234-1234")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy_wrong_id(self):
        """ test destroy with id that doesn't exist """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234-1234-1234")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    #######
    # all #
    #######

    def test_all(self):
        """ test all """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        test_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(test_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")

    def test_help(self):
        """ test console """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertEqual(f.getvalue(), "Prints the string representation \
of an instance based on the class name and id\n")
