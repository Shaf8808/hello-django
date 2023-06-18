from django.test import TestCase
from .models import Item


# Create your tests here.
class TestViews(TestCase):

    def test_get_todo_list(self):
        # Checks if the response retrieves the homepage
        response = self.client.get('/')
        # Confirms if the status code is a successful
        # HTTP response (200)
        self.assertEqual(response.status_code, 200)
        # Confirms if the view uses the correct template
        # (todo_list.html)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        # Checks if the response retrieves the homepage
        response = self.client.get('/add')
        # Confirms if the status code is a successful
        # HTTP response (200)
        self.assertEqual(response.status_code, 200)
        # Confirms if the view uses the correct template
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # Checks if the response retrieves the homepage
        response = self.client.get('/edit/99')
        # Confirms if the status code is a successful
        # HTTP response (200)
        self.assertEqual(response.status_code, 200)
        # Confirms if the view uses the correct template
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # def test_can_add_item(self):

    # def test_can_delete_item(self):

    # def test_can_toggle_item(self):
