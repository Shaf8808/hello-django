from django.test import TestCase
from .forms import ItemForm


# Create your tests here.
class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # If a user tries to submit the form without
        # filling out the name field
        form = ItemForm({'name': ''})
        # Makes sure the form is not valid
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_meta_class(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
