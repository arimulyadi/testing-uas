from django.test import SimpleTestCase
from django.urls import resolve, reverse

from tasks.views import tasks, complete, delete

class TestUrls(SimpleTestCase):

	def test_task_url(self):
		url = reverse('tasks')
		self.assertEquals(resolve(url).func, tasks)
	
	def test_complete_url(self):
		url = reverse('completed_task', args=[1])
		self.assertEquals(resolve(url).func, complete)

	def test_delete_url(self):
		url = reverse('delete_task', args=[1])
		self.assertEquals(resolve(url).func, delete)