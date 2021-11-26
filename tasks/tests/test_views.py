from django.conf.urls import url
from django.http import response
from django.test import Client, TestCase, client
from django.urls import resolve, reverse
# from tasks.models import Username
from  tasks.models import Username

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.tasks_url = reverse('tasks')
        self.complete_url = reverse('completed_task', args=[1])
        self.delete_url = reverse('delete_task', args=[1])
        self.user = Username.objects.create(username="arimulyadi")


    def test_tasks_get(self):
        response = self.client.get(self.tasks_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    # def test_tasks_post(self):
    #     data = {
    #         'title':'task title',
    #         'description':'task deskripsi',
    #         'date_of_creation':'2021-11-26 04:24:50',
    #         'complete':0,
    #         'username_id':self.user.id,
    #         'priority':'adanger'
    #     }
    #     response = self.client.post(self.tasks_url, data)


    def test_complete_task(self):
        response = self.client.get(self.complete_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, '/')

    def test_delete(self):
        response = self.client.get(self.delete_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'tasks')
