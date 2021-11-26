from django.test import TestCase
from tasks.models import Username, Task

class TestModels(TestCase):
	
	def setUp(self):
		self.user = Username.objects.create(username="arimulyadi")
		self.task = Task.objects.create(
							title="task title",
							description="task deskripsi",
							date_of_creation="2021-11-26 04:24:50",
							complete=0,
							username_id=self.user.id,
							priority="adanger"
						)

	def test_username(self):
		self.assertEquals(self.user.username, "arimulyadi")

	def test_task(self):
		temp_task = Task.objects.get(id=self.task.id)
		self.assertEquals(self.task.id, temp_task.id)
