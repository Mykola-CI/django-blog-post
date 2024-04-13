from django.test import TestCase
from django.urls import reverse
from .forms import CollaborateForm

class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Myke',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)