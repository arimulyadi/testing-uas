from django.conf.urls import url
from django.http import response
from django.test import Client, TestCase, client
from django.urls import resolve, reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.tasks_url = reverse('tasks')
        self.complete_url = reverse('completed_task', args=[0])
        self.delete_url = reverse('delete_task', args=[0])

    def test_tasks(self):
        response = self.client.get(self.tasks_url)

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'tasks.html')

    def test_complete(self):
        response = self.client.get(self.complete_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, '/')

    def test_delete(self):
        response = self.client.get(self.delete_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'tasks')
