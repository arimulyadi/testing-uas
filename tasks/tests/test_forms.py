from django.test import SimpleTestCase
from tasks.models import   TaskForm, UsernameForm

class TestForm(SimpleTestCase):

    def test_taskform(self):
        form = TaskForm(data={
            'title': 'Whats on your mind today',
            'description': "Describe your task ..", 
            'cols': 80, 
            'rows': 3
        })
        self.assertTrue(form.is_valid())
        
    def test_taskform(self):
        form = TaskForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


    def test_usernameform(self):
        form = UsernameForm(data={
            'username': "Enter a username"
        })
        self.assertTrue(form.is_valid())
        
    def test_usernameform(self):
        form = UsernameForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)