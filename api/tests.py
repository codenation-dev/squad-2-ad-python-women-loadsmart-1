from django.test import TestCase
from rest_framework.test import APITestCase
from api.models import Event, Agent, Environment
from users.models import CustomUser

# Create your tests here.
class TestSerializer(APITestCase):
    def test_do_something(self):
        test_env = Environment.objects.create(name="Dev")
        test_agent = Agent.objects.create(env=test_env)
        test_user = CustomUser.objects.create(first_name="Marcela", last_name="Vieira", email="marcela@gmail.com", password="newpassword654")
        test_event = Event.objects.create(level="C", agent=test_agent, user=test_user)
        # address =
        self.assertTrue(True)
